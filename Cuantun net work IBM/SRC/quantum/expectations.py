import numpy as np
import time
from qiskit.transpiler import PassManager
from qiskit.transpiler.passes import Optimize1qGatesDecomposition

try:
    from qiskit.primitives import Estimator as BaseEstimator  # FIX: Renombrar
    from qiskit.quantum_info import Pauli, SparsePauliOp
    from qiskit.compiler import transpile
HAVE_QISKIT = True
except Exception as e:
    print(f"Qiskit import warning: {e}")
    HAVE_QISKIT = False

def z_observables(n_qubits):
    """Genera observables Z para cada qubit"""
    obs = []
    for i in range(n_qubits):
        s = ["I"] * n_qubits
        s[i] = "Z"
        obs.append(Pauli("".join(s)))
    return obs

def get_quantum_backend(cfg, n_qubits):
    """Obtiene backend cuántico (simulador o hardware real)"""
    ibm_config = cfg.get("ibm_quantum", {})
    
    if ibm_config.get("service_available", False) and ibm_config.get("use_real_hardware", False):
        try:
            service = QiskitRuntimeService()

            backends = service.backends(
                min_num_qubits=n_qubits,
                operational=True,
                simulator=False
            )
            if backends:
                backend_name = ibm_config.get("preferred_backend")
                if backend_name:
                    backend = service.get_backend(backend_name)
                else:
                    backend = backends[0]  # Usar el primero disponible
                print(f"Using IBM Quantum backend: {backend.name}")
                return backend, True
        except Exception as e:
            print(f"Could not connect to IBM Quantum hardware: {e}")
    

    print("Using AerSimulator")
    return AerSimulator(method="automatic"), False

def transpile_for_hardware(qc, backend):
    """Transpila circuito para hardware específico"""

    pass_manager = PassManager([Optimize1qGatesDecomposition(['ry', 'rx', 'rz'])])
    qc_optimized = pass_manager.run(qc)
    

    qc_transpiled = transpile(
        qc_optimized,
        backend=backend,
        optimization_level=3
    )
    
    return qc_transpiled

def expectations_for_angles(angles, cfg, shots=1024, entanglement_layers=1):
    """Calcula expectativas usando IBM Quantum o simulador"""
    if not HAVE_QISKIT:
        return [0.0] * len(angles) if angles else []
    
    n = len(angles)
    if n == 0:
        return []
    
    backend, is_real_hardware = get_quantum_backend(cfg, n)
    
    from .circuits import build_hardware_efficient_ansatz
    qc = build_hardware_efficient_ansatz(angles, depth=entanglement_layers)
    
    if qc is None:
        return [0.0] * n
    
    if is_real_hardware:
        qc = transpile_for_hardware(qc, backend)
    
    obs = z_observables(n)
    
    try:
        if is_real_hardware:
         
            service = QiskitRuntimeService()
            with Session(service=service, backend=backend) as session:
                estimator = RuntimeEstimator(session=session) 
                job = estimator.run(
                    circuits=[qc] * len(obs),
                    observables=obs,
                    shots=shots
                )
                result = job.result()
                values = [float(v) for v in result.values]
        else:
         
            estimator = BaseEstimator()  
            jobs = [(qc, o) for o in obs]  
            result = estimator.run(jobs, shots=shots).result()
            values = [float(v) for v in result.values]
        
        return values
        
    except Exception as e:
        print(f"Quantum computation failed: {e}")

        return [np.tanh(angle) * 0.8 for angle in angles] if angles else []

def batch_quantum_computations(angle_batches, cfg):
    """Procesa lotes de computación cuántica de manera eficiente"""
    results = []
    
    for i, angles in enumerate(angle_batches):
        if i > 0 and i % 10 == 0:
            print(f"Processed {i}/{len(angle_batches)} quantum batches")
        
        exps = expectations_for_angles(angles, cfg)
        results.append(exps)
        

        if cfg.get("ibm_quantum", {}).get("service_available", False):
            time.sleep(0.5)
    
    return results