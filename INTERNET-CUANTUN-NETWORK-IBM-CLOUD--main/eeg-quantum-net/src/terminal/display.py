import os
from typing import Dict


class TerminalDisplay:
    
    def __init__(self):
        pass
    
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def render(self, metrics):
        self.clear()
        
        print("=" * 80)
        print("  WINDOWS POWERSHELL - SCSC QUANTUM SECURITY MODULE")
        print("  PS C:\\quantum\\SCSC>")
        print("=" * 80)
        print()
        
        print("┌─ SYSTEM METRICS " + "─" * 60 + "┐")
        print(f"│ CPU Usage:        {metrics['cpu_usage']:>6.1f}%                                                         │")
        print(f"│ Memory:           {metrics['memory_used']:>5.1f}/{metrics['memory_total']:>5.1f} GB                                                  │")
        print(f"│ Quantum Fidelity: {metrics['quantum_fidelity']:>8.4f}                                                     │")
        print(f"│ QBER:             {metrics['qber']:>6.2f}%                                                         │")
        print(f"│ Entangled Qubits: {metrics['entangled_qubits']:>2d}/{metrics['total_qubits']:<2d}                                                        │")
        print(f"│ Throughput:       {metrics['throughput']:>6,d} ops/s                                                   │")
        print(f"│ Avg Latency:      {metrics['avg_latency']:>6.1f}ms                                                       │")
        print("└" + "─" * 78 + "┘")
        print()
        
        print("┌─ POST-QUANTUM CRYPTO " + "─" * 57 + "┐")
        print("│ Algorithm:        Kyber-1024 (lattice)                                                  │")
        print("│ Signature:        SPHINCS+                                                              │")
        print("│ QKD Protocol:     BB84 (Simulated)                                                      │")
        print(f"│ Keys Distributed: {metrics['keys_distributed']:>3d}                                                          │")
        print(f"│ Attacks Blocked:  {metrics['attacks_blocked']:>3d}                                                          │")
        print("└" + "─" * 78 + "┘")
        print()
        
        print("┌─ CLUSTER NODES (5/5 ACTIVE) " + "─" * 51 + "┐")
        print("│ MASTER [192.168.1.100] - ACTIVE                                                       │")
        for node, latency in metrics['heartbeats'].items():
            status = "●" if latency < 2.5 else "○"
            node_num = node.split("-")[1]
            print(f"│ {node} [192.168.1.{node_num}] - heartbeat {latency:.1f}ms {status}                                                   │")
        print("└" + "─" * 78 + "┘")
        print()
        
        print("┌─ COMMANDS " + "─" * 68 + "┐")
        print("│  help     - Mostrar ayuda                                                              │")
        print("│  status   - Mostrar estado del sistema                                                 │")
        print("│  crypto   - Mostrar información de criptografía                                        │")
        print("│  quantum  - Ejecutar circuito cuántico                                                 │")
        print("│  attack   - Simular un ataque cibernético                                              │")
        print("│  clear    - Limpiar la pantalla                                                        │")
        print("│  exit     - Salir de la terminal                                                       │")
        print("└" + "─" * 78 + "┘")
        print()
        
        print("┌─ EVENT LOG " + "─" * 68 + "┐")
        for log in metrics['event_logs'][:10]:
            if len(log) > 68:
                log = log[:65] + "..."
            print(f"│ {log:<76}│")
        print("└" + "─" * 78 + "┘")
        print()
        
        print("-" * 80)
        print("  PS> ", end="", flush=True)