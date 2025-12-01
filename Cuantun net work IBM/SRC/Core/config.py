import yaml
from pathlib import Path
import os
from qiskit_ibm_runtime import QiskitRuntimeService

def load_config(path="config/default.yaml"):
    with open(path, "r") as f:
        cfg = yaml.safe_load(f)
    

    for k in ("artifacts_dir", "models_dir", "reports_dir"):
        Path(cfg.get(k, ".")).mkdir(parents=True, exist_ok=True)

    ibm_config = cfg.get("ibm_quantum", {})
    if ibm_config.get("enabled", False):
        try:

            token = ibm_config.get("token") or os.getenv("IBM_QUANTUM_TOKEN")
            if token:
                QiskitRuntimeService.save_account(
                    channel="ibm_quantum",
                    token=token,
                    instance=ibm_config.get("instance", "ibm-q/open/main"),
                    overwrite=True
                )
                cfg["ibm_quantum"]["service_available"] = True
                print("IBM Quantum account configured successfully")
            else:
                cfg["ibm_quantum"]["service_available"] = False
                print("IBM Quantum token not found, using simulators")
        except Exception as e:
            print(f"IBM Quantum configuration failed: {e}")
            cfg["ibm_quantum"]["service_available"] = False
    
    return cfg