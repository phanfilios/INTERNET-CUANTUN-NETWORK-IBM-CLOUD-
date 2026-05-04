import time
import threading
import random

from .metrics import SystemMetrics
from .display import TerminalDisplay


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
            print("\n[INFO] Cerrando...")
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
        print("\n  Iniciando Quantum Security Terminal...\n")
        time.sleep(1)
        
        update_thread = threading.Thread(target=self._update_loop, daemon=True)
        update_thread.start()
        
        self._command_loop()


def main():
    terminal = QuantumTerminal()
    try:
        terminal.run()
    except KeyboardInterrupt:
        print("\n\n[INFO] Terminal cerrada")
    except Exception as e:
        print(f"\n[ERROR] {e}")


if __name__ == "__main__":
    main()