"""
Quantum Security Terminal - SCSC v3.1.4
Ejecutar con: python quantum_terminal.py
"""

import random
import time
import threading
import os
from datetime import datetime
from typing import Dict, List


# ============================================================
# MÓDULO DE MÉTRICAS
# ============================================================

class SystemMetrics:
    
    def __init__(self):
        self.cpu_usage = 22.7
        self.memory_used = 8.7
        self.memory_total = 32.0
        self.quantum_fidelity = 0.9992
        self.qber = 1.5
        self.entangled_qubits = 11
        self.total_qubits = 24
        self.throughput = 1239
        self.avg_latency = 16.9
        self.keys_distributed = 46
        self.attacks_blocked = 128
        
        self.heartbeat_latencies = {
            "NODE-01": 1.2,
            "NODE-02": 1.5,
            "NODE-03": 1.1,
            "NODE-04": 2.3,
            "NODE-05": 1.8
        }
        
        self.event_logs = []
        self._init_logs()
    
    def _init_logs(self):
        self.event_logs = [
            "[10:54:05 PM] Heartbeat from NODE-05 (2.7ms)",
            "[10:54:48 PM] No-cloning theorem verified",
            "[10:55:08 PM] Quantum fluctuation corrected",
            "[10:56:00 PM] Kyber-1024 key generated",
            "[10:56:09 PM] EPR entanglement: nodes 1 and 3"
        ]
    
    def update(self):
        self.cpu_usage = round(15 + random.random() * 20, 1)
        self.memory_used = round(6 + random.random() * 6, 1)
        self.quantum_fidelity = round(0.998 + random.random() * 0.0018, 4)
        self.qber = round(0.8 + random.random() * 1.7, 2)
        
        delta = random.choice([-1, 0, 0, 0, 0, 1, 1])
        self.entangled_qubits += delta
        self.entangled_qubits = max(0, min(self.total_qubits, self.entangled_qubits))
        
        self.throughput = 1000 + random.randint(0, 500)
        self.avg_latency = round(12 + random.random() * 10, 1)
        
        for node in self.heartbeat_latencies:
            variation = random.uniform(-0.3, 0.3)
            new_value = self.heartbeat_latencies[node] + variation
            self.heartbeat_latencies[node] = round(max(0.5, min(5.0, new_value)), 1)
    
    def add_event(self, message):
        timestamp = datetime.now().strftime("%I:%M:%S %p").lower()
        self.event_logs.insert(0, f"[{timestamp}] {message}")
        if len(self.event_logs) > 12:
            self.event_logs = self.event_logs[:12]
    
    def random_event(self):
        nodes = list(self.heartbeat_latencies.keys())
        events = [
            f"Heartbeat {random.choice(nodes)} ({random.uniform(0.8, 3.5):.1f}ms)",
            "No-cloning theorem verified",
            "EPR entanglement established",
            "Quantum fluctuation corrected",
            "Kyber-1024 key generated"
        ]
        self.add_event(random.choice(events))
    
    def to_dict(self):
        return {
            "cpu_usage": self.cpu_usage,
            "memory_used": self.memory_used,
            "memory_total": self.memory_total,
            "quantum_fidelity": self.quantum_fidelity,
            "qber": self.qber,
            "entangled_qubits": self.entangled_qubits,
            "total_qubits": self.total_qubits,
            "throughput": self.throughput,
            "avg_latency": self.avg_latency,
            "heartbeats": self.heartbeat_latencies.copy(),
            "keys_distributed": self.keys_distributed,
            "attacks_blocked": self.attacks_blocked,
            "event_logs": self.event_logs.copy()
        }


# ============================================================
# MÓDULO DE VISUALIZACIÓN
# ============================================================

class TerminalDisplay:
    
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def render(self, metrics):
        self.clear()
        
        print("=" * 80)
        print("  WINDOWS POWERSHELL - SCSC QUANTUM SECURITY MODULE")
        print("  PS C:\\quantum\\SCSC>")
        print("=" * 80)
        print()
        
        # System Metrics
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
        
        # Post-Quantum Crypto
        print("┌─ POST-QUANTUM CRYPTO " + "─" * 57 + "┐")
        print("│ Algorithm:        Kyber-1024 (lattice)                                                  │")
        print("│ Signature:        SPHINCS+                                                              │")
        print("│ QKD Protocol:     BB84 (Simulated)                                                      │")
        print(f"│ Keys Distributed: {metrics['keys_distributed']:>3d}                                                          │")
        print(f"│ Attacks Blocked:  {metrics['attacks_blocked']:>3d}                                                          │")
        print("└" + "─" * 78 + "┘")
        print()
        
        # Cluster Nodes
        print("┌─ CLUSTER NODES (5/5 ACTIVE) " + "─" * 51 + "┐")
        print("│ MASTER [192.168.1.100] - ACTIVE                                                       │")
        for node, latency in metrics['heartbeats'].items():
            status = "●" if latency < 2.5 else "○"
            node_num = node.split("-")[1]
            print(f"│ {node} [192.168.1.{node_num}] - heartbeat {latency:.1f}ms {status}                                                   │")
        print("└" + "─" * 78 + "┘")
        print()
        
        # Commands
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
        
        # Event Log
        print("┌─ EVENT LOG " + "─" * 68 + "┐")
        for log in metrics['event_logs'][:10]:
            if len(log) > 68:
                log = log[:65] + "..."
            print(f"│ {log:<76}│")
        print("└" + "─" * 78 + "┘")
        print()
        
        print("-" * 80)
        print("  PS> ", end="", flush=True)


# ============================================================
# MÓDULO PRINCIPAL
# ============================================================

class QuantumTerminal:
    
    def __init__(self):
        self.metrics = SystemMetrics()
        self.display = TerminalDisplay()
        self.running = True
    
    def _update_loop(self):
        while self.running:
            self.metrics.update()
            if random.random() < 0.1:
                self.metrics.random_event()
            self.display.render(self.metrics.to_dict())
            time.sleep(1)
    
    def _show_help(self):
        print("\n" + "=" * 60)
        print("  COMANDOS DISPONIBLES")
        print("=" * 60)
        print("  help      - Muestra esta ayuda")
        print("  status    - Estado del sistema")
        print("  crypto    - Info de criptografía")
        print("  quantum   - Ejecutar circuito cuántico")
        print("  attack    - Simular ataque")
        print("  clear     - Limpiar pantalla")
        print("  exit      - Salir")
        print("=" * 60)
        input("\nPresione ENTER...")
    
    def _show_status(self):
        m = self.metrics.to_dict()
        print("\n" + "=" * 60)
        print("  ESTADO DEL SISTEMA")
        print("=" * 60)
        print(f"  CPU:             {m['cpu_usage']:.1f}%")
        print(f"  Memory:          {m['memory_used']:.1f}/{m['memory_total']:.1f} GB")
        print(f"  Quantum Fidelity: {m['quantum_fidelity']:.4f}")
        print(f"  QBER:            {m['qber']:.2f}%")
        print(f"  Entangled:       {m['entangled_qubits']}/{m['total_qubits']}")
        print(f"  Throughput:      {m['throughput']:,} ops/s")
        print(f"  Latency:         {m['avg_latency']:.1f}ms")
        print(f"  Attacks Blocked: {m['attacks_blocked']}")
        print("=" * 60)
        input("\nPresione ENTER...")
    
    def _show_crypto(self):
        m = self.metrics.to_dict()
        print("\n" + "=" * 60)
        print("  CRIPTOGRAFÍA POST-CUÁNTICA")
        print("=" * 60)
        print("  Algorithm:   Kyber-1024")
        print("  Signature:   SPHINCS+")
        print("  QKD:         BB84")
        print("-" * 60)
        print(f"  Keys:        {m['keys_distributed']}")
        print(f"  Attacks:     {m['attacks_blocked']}")
        print("=" * 60)
        input("\nPresione ENTER...")
    
    def _execute_quantum(self):
        print("\n" + "=" * 60)
        print("  ⚛️  EJECUTANDO CIRCUITO CUÁNTICO")
        print("=" * 60)
        
        for p in range(0, 101, 25):
            print(f"  Procesando... {p}%", end="\r")
            time.sleep(0.3)
        print("  Procesando... 100%")
        time.sleep(0.5)
        
        print("\n  ✓ Circuito ejecutado")
        print("    Tipo: EPR + BB84")
        print("    Qubits: 4")
        print("    |00⟩: 487 (47.6%)")
        print("    |11⟩: 537 (52.4%)")
        
        self.metrics.entangled_qubits = min(24, self.metrics.entangled_qubits + 1)
        self.metrics.add_event("Circuito cuántico ejecutado")
        print("=" * 60)
        input("\nPresione ENTER...")
    
    def _simulate_attack(self):
        attacks = ["MITM", "Eavesdropping", "Replay", "Quantum Hijack"]
        nodes = list(self.metrics.heartbeat_latencies.keys())
        
        attack = random.choice(attacks)
        target = random.choice(nodes)
        
        print("\n" + "=" * 60)
        print("  ⚠️  INTRUSIÓN DETECTADA")
        print("=" * 60)
        print(f"  Ataque: {attack}")
        print(f"  Target: {target}")
        time.sleep(0.8)
        
        if random.random() < 0.95:
            print("  ✓ Ataque neutralizado")
            self.metrics.attacks_blocked += 1
            self.metrics.add_event(f"Ataque bloqueado: {attack}")
        else:
            print("  ✗ Brecha parcial")
            self.metrics.add_event(f"Brecha: {attack}")
        
        print("=" * 60)
        input("\nPresione ENTER...")
    
    def _process_command(self, cmd):
        c = cmd.strip().lower()
        
        if c in ["help", "h", "?"]:
            self._show_help()
        elif c == "status":
            self._show_status()
        elif c == "crypto":
            self._show_crypto()
        elif c == "quantum":
            self._execute_quantum()
        elif c == "attack":
            self._simulate_attack()
        elif c == "clear":
            self.display.clear()
            self.display.render(self.metrics.to_dict())
        elif c in ["exit", "quit", "q"]:
            print("\n[INFO] Cerrando sistema de seguridad cuántica...")
            self.running = False
        elif c:
            print(f"\n[ERROR] Comando '{c}' no reconocido")
            time.sleep(1)
    
    def _command_loop(self):
        while self.running:
            try:
                cmd = input()
                self._process_command(cmd)
            except KeyboardInterrupt:
                print("\n")
    
    def run(self):
        print("\n  Iniciando Quantum Security Terminal v3.1.4...")
        print("  Conectando con IBM Quantum Backend...")
        time.sleep(2)
        
        update_thread = threading.Thread(target=self._update_loop, daemon=True)
        update_thread.start()
        
        self._command_loop()


# ============================================================
# PUNTO DE ENTRADA
# ============================================================

if __name__ == "__main__":
    terminal = QuantumTerminal()
    try:
        terminal.run()
    except KeyboardInterrupt:
        print("\n\n[INFO] Terminal cerrada")
    except Exception as e:
        print(f"\n[ERROR] {e}")