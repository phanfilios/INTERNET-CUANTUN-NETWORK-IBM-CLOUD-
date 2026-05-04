import numpy as np
from typing import Optional, Dict, Any, Tuple
import random


class QuantumCircuitSimulator:
    """Simulador de circuitos cuánticos para EPR, BB84, etc."""
    
    def __init__(self):
        self.epr_pairs = []
        self.bb84_keys = []
    
    def create_epr_pair(self) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        """
        Simula la creación de un par EPR (estado de Bell)
        
        Returns:
            Tuple de dos qubits entrelazados
        """
        # Simular estado de Bell |Φ+⟩ = (|00⟩ + |11⟩)/√2
        measurement = random.choice(["00", "11"])
        
        qubit_a = {
            "id": f"q_{len(self.epr_pairs)}_a",
            "state": measurement[0],
            "entangled_with": None
        }
        
        qubit_b = {
            "id": f"q_{len(self.epr_pairs)}_b", 
            "state": measurement[1],
            "entangled_with": qubit_a["id"]
        }
        
        qubit_a["entangled_with"] = qubit_b["id"]
        
        self.epr_pairs.append((qubit_a, qubit_b))
        
        return qubit_a, qubit_b
    
    def bb84_simulate(self, num_bits: int = 128) -> Dict[str, Any]:
        """
        Simula el protocolo BB84 para distribución de claves cuánticas
        
        Args:
            num_bits: Número de bits a generar
            
        Returns:
            Diccionario con la clave generada y estadísticas
        """
        # Bases: 0 = rectilínea (Z), 1 = diagonal (X)
        alice_bases = [random.randint(0, 1) for _ in range(num_bits)]
        bob_bases = [random.randint(0, 1) for _ in range(num_bits)]
        
        # Bits originales de Alice
        alice_bits = [random.randint(0, 1) for _ in range(num_bits)]
        
        # Simular transmisión con ruido cuántico (QBER ~1-3%)
        qber = 0.015  # 1.5%
        bob_bits = []
        
        for i in range(num_bits):
            if alice_bases[i] == bob_bases[i]:
                # Misma base - bit correcto con probabilidad 1-QBER
                if random.random() > qber:
                    bob_bits.append(alice_bits[i])
                else:
                    bob_bits.append(1 - alice_bits[i])
            else:
                # Diferente base - bit aleatorio
                bob_bits.append(random.randint(0, 1))
        
        # Filtrar donde las bases coinciden
        sifted_key = []
        for i in range(num_bits):
            if alice_bases[i] == bob_bases[i]:
                sifted_key.append(alice_bits[i])
        
        # Tomar primeros 256 bits como clave
        final_key = sifted_key[:256] if len(sifted_key) >= 256 else sifted_key
        
        # Estadísticas
        matching_bases = sum(1 for a, b in zip(alice_bases, bob_bases) if a == b)
        error_rate = sum(1 for i in range(min(num_bits, len(bob_bits))) 
                        if alice_bases[i] == bob_bases[i] and alice_bits[i] != bob_bits[i]) / max(1, matching_bases)
        
        result = {
            "key": final_key,
            "key_hex": self._bits_to_hex(final_key),
            "key_length": len(final_key),
            "matching_bases": matching_bases,
            "qber_simulated": error_rate * 100,
            "bits_sent": num_bits
        }
        
        self.bb84_keys.append(result)
        return result
    
    def _bits_to_hex(self, bits: list) -> str:
        """Convierte lista de bits a string hexadecimal"""
        # Asegurar longitud múltiplo de 4
        padded = bits + [0] * ((4 - len(bits) % 4) % 4)
        hex_str = ""
        for i in range(0, len(padded), 4):
            nibble = padded[i:i+4]
            val = sum(b << (3 - j) for j, b in enumerate(nibble))
            hex_str += f"{val:x}"
        return hex_str
    
    def run_teleportation(self) -> Dict[str, Any]:
        """Simula teletransportación cuántica"""
        # Estado a teletransportar: |ψ⟩ = α|0⟩ + β|1⟩
        alpha = random.uniform(0, 1)
        beta = np.sqrt(1 - alpha**2)
        
        # Crear par EPR
        qubit_a, qubit_b = self.create_epr_pair()
        
        # Simular medición de Bell
        bell_measurement = random.choice(["Φ+", "Φ-", "Ψ+", "Ψ-"])
        
        # Aplicar corrección según medición
        if bell_measurement == "Φ-":
            correction = "Z"
        elif bell_measurement == "Ψ+":
            correction = "X"
        elif bell_measurement == "Ψ-":
            correction = "Z then X"
        else:
            correction = "None"
        
        result = {
            "original_state": {"alpha": round(alpha, 3), "beta": round(beta, 3)},
            "bell_measurement": bell_measurement,
            "correction_applied": correction,
            "fidelity": 0.999 - random.uniform(0, 0.005),
            "success": True
        }
        
        return result
    
    def execute_circuit(self, circuit_type: str = "epr", **kwargs) -> Dict[str, Any]:
        """
        Ejecuta diferentes tipos de circuitos cuánticos
        
        Args:
            circuit_type: "epr", "bb84", "teleport", "random"
            **kwargs: Argumentos adicionales
            
        Returns:
            Resultados del circuito
        """
        if circuit_type == "epr":
            qubit_a, qubit_b = self.create_epr_pair()
            return {
                "type": "EPR",
                "qubit_a": qubit_a,
                "qubit_b": qubit_b,
                "state": f"Bell state |Φ+⟩ = (|00⟩ + |11⟩)/√2",
                "fidelity": 0.998
            }
        elif circuit_type == "bb84":
            num_bits = kwargs.get("num_bits", 128)
            return self.bb84_simulate(num_bits)
        elif circuit_type == "teleport":
            return self.run_teleportation()
        else:
            # Circuito aleatorio con puertas
            gates = ["H", "X", "Z", "CNOT", "RY"]
            selected = random.sample(gates, k=random.randint(2, 4))
            return {
                "type": "RANDOM",
                "gates": selected,
                "qubits_used": 2 + random.randint(0, 2),
                "depth": len(selected),
                "success": True
            }