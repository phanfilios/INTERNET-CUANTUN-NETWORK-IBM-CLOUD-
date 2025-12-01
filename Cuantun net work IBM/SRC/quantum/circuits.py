from typing import Optional, List
import numpy as np

try:
    from qiskit import QuantumCircuit
    HAVE_QISKIT = True
except ImportError:
    HAVE_QISKIT = False
    print("Qiskit not available, quantum features disabled")

def build_ansatz(angles: List[float], entanglement_layers: int = 1, hardware_aware: bool = True) -> Optional[QuantumCircuit]:
    """Construye circuito ansatz para computación cuántica"""
    if not HAVE_QISKIT:
        return None
    
    n = len(angles)
    qc = QuantumCircuit(n)
    

    for i, theta in enumerate(angles):
        qc.ry(theta, i)
    

    for layer in range(entanglement_layers):
      
        if hardware_aware and n > 1:
           
            for i in range(0, n-1):
                qc.cx(i, i+1)
        else:
          
            for i in range(0, n-1, 2):
                if i + 1 < n:  
                    qc.cx(i, i+1)
            for i in range(1, n-1, 2):
                if i + 1 < n:  
                    qc.cx(i, i+1)
        
       
        for i, theta in enumerate(angles):
            qc.ry(0.3 * theta * (layer + 1), i)
    
    return qc

def build_hardware_efficient_ansatz(angles: List[float], depth: int = 2) -> Optional[QuantumCircuit]:
    """Ansatz más eficiente para hardware real"""
    if not HAVE_QISKIT:
        return None
    
    n = len(angles)
    qc = QuantumCircuit(n)
    
    for d in range(depth):
        
        for i in range(n):
            qc.ry(angles[i] * (d + 1) / depth, i)
        
 
        if n > 1:
            for i in range(0, n-1):
                qc.cx(i, i+1)
    
    return qc