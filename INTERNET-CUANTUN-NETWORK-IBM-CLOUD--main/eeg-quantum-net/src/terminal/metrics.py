import random
from datetime import datetime
from typing import Dict, List


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
            "[10:54:05 PM] Heartbeat received from NODE-05 (latency: 2.7ms)",
            "[10:54:48 PM] No-cloning theorem verified",
            "[10:55:08 PM] Quantum fluctuation detected - Correction applied",
            "[10:56:00 PM] Kyber-1024 key generated",
            "[10:56:09 PM] EPR entanglement established"
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
            f"Heartbeat from {random.choice(nodes)} ({random.uniform(0.8, 3.5):.1f}ms)",
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