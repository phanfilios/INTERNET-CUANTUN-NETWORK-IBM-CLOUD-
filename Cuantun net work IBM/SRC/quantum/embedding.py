from typing import List
import numpy as np

def expand_to_angles(band_means: List[float], alpha: float = 1.5, scale: float = 0.01, 
                    target_qubits: int = 100) -> List[float]:
    """Expande las medias de bandas a ángulos para circuitos cuánticos"""
    if not band_means:
        return [0.0] * target_qubits
    
    base = [alpha * np.tanh(scale * float(m)) for m in band_means]
    reps = target_qubits // len(base) + 1
    tiled = (base * reps)[:target_qubits]
    

    idx = np.arange(target_qubits)
    jitter = 0.05 * np.sin(idx / 7.0)
    
    return list((np.array(tiled) + jitter).astype(float))