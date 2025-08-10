"""
Classical vs Quantum Systems Simulation / Klasik vs Kuantum Sistemler Simülasyonu

This project demonstrates the fundamental differences between classical and quantum systems:
- Classical systems: Deterministic behavior with definite outcomes
- Quantum systems: Probabilistic behavior with superposition states

Bu proje, klasik ve kuantum sistemlerin temel farklarını gösterir:
- Klasik sistemler: Deterministik davranış, kesin sonuçlar
- Kuantum sistemler: Olasılıksal davranış, süperpozisyon durumları

Author: Muhammed Semih Külekçioğlu
Date: August 2025
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, List
import random

# Dil seçimi için metin sözlükleri
LANGUAGES = {
    'tr': {
        'title': '🔬 KLASİK vs KUANTUM SİSTEMLER DEMO\'SU',
        'classical_system': '📊 1. KLASİK SİSTEM:',
        'quantum_system': '⚛️ 2. KUANTUM SİSTEM:',
        'initial_state': 'Başlangıç durumu',
        'measurements_deterministic': 'Ölçümler (deterministik):',
        'measurement': 'Ölçüm',
        'state_changed': 'Durum değiştirildi',
        'measurements_after_change': 'Tekrar ölçümler:',
        'measurements_probabilistic': 'Ölçümler (olasılıksal):',
        'creating_superposition': 'Süperpozisyon yaratılıyor...',
        'superposition_created': 'Süperpozisyon yaratıldı',
        'measurements_in_superposition': 'Süperpozisyon durumunda ölçümler:',
        'applying_hadamard': 'Hadamard kapısı uygulanıyor...',
        'hadamard_applied': 'Hadamard kapısı uygulandı',
        'new_state': 'Yeni durum',
        'measurements_in_new_state': 'Yeni durumda ölçümler:',
        'drawing_plot': '📈 DURUM EVRİMİ GRAFİĞİ ÇİZİLİYOR...',
        'classical_title': 'Klasik Sistem - Deterministik Davranış',
        'quantum_title': 'Kuantum Sistem - Olasılıksal Davranış',
        'state': 'Durum',
        'measurement_sequence': 'Ölçüm Sırası',
        'interactive_demo': '🎮 ETKİLEŞİMLİ DEMO',
        'options': 'Seçenekler:',
        'classical_demo': '1. Klasik sistem demo',
        'quantum_demo': '2. Kuantum sistem demo',
        'state_evolution': '3. Durum evrimi grafiği',
        'exit': '4. Çıkış',
        'make_choice': 'Seçiminizi yapın (1-4):',
        'classical_demo_title': '📊 KLASİK SİSTEM DEMO:',
        'enter_new_state': 'Yeni durum girin (0 veya 1):',
        'state_changed_to': 'Durum değiştirildi',
        'invalid_state': '❌ Geçersiz durum! Sadece 0 veya 1 girin.',
        'quantum_demo_title': '⚛️ KUANTUM SİSTEM DEMO:',
        'enter_alpha': 'α değerini girin (gerçel sayı):',
        'enter_beta': 'β değerini girin (gerçel sayı):',
        'apply_hadamard_question': 'Hadamard kapısı uygulansın mı? (e/h):',
        'error': '❌ Hata',
        'ending_demo': '👋 Demo sonlandırılıyor...',
        'invalid_choice': '❌ Geçersiz seçim! Lütfen 1-4 arası bir sayı girin.',
        'superposition_not_possible': '❌ Klasik sistemlerde süperpozisyon mümkün değil!',
        'system_single_state': '   Sistem sadece tek bir durumda bulunabilir.',
        'superposition_created_msg': '✅ Süperpozisyon yaratıldı',
        'hadamard_gate_applied': '🔀 Hadamard kapısı uygulandı',
        'new_state_vector': '   Yeni durum'
    },
    'en': {
        'title': '🔬 CLASSICAL vs QUANTUM SYSTEMS DEMONSTRATION',
        'classical_system': '📊 1. CLASSICAL SYSTEM:',
        'quantum_system': '⚛️ 2. QUANTUM SYSTEM:',
        'initial_state': 'Initial state',
        'measurements_deterministic': 'Measurements (deterministic):',
        'measurement': 'Measurement',
        'state_changed': 'State changed to',
        'measurements_after_change': 'Measurements after state change:',
        'measurements_probabilistic': 'Measurements (probabilistic):',
        'creating_superposition': 'Creating superposition...',
        'superposition_created': 'Superposition created',
        'measurements_in_superposition': 'Measurements in superposition state:',
        'applying_hadamard': 'Applying Hadamard gate...',
        'hadamard_applied': 'Hadamard gate applied',
        'new_state': 'New state',
        'measurements_in_new_state': 'Measurements in new state:',
        'drawing_plot': '📈 DRAWING STATE EVOLUTION PLOT...',
        'classical_title': 'Classical System - Deterministic Behavior',
        'quantum_title': 'Quantum System - Probabilistic Behavior',
        'state': 'State',
        'measurement_sequence': 'Measurement Sequence',
        'interactive_demo': '🎮 INTERACTIVE DEMONSTRATION',
        'options': 'Options:',
        'classical_demo': '1. Classical system demo',
        'quantum_demo': '2. Quantum system demo',
        'state_evolution': '3. State evolution plot',
        'exit': '4. Exit',
        'make_choice': 'Make your choice (1-4):',
        'classical_demo_title': '📊 CLASSICAL SYSTEM DEMO:',
        'enter_new_state': 'Enter new state (0 or 1):',
        'state_changed_to': 'State changed to',
        'invalid_state': '❌ Invalid state! Please enter only 0 or 1.',
        'quantum_demo_title': '⚛️ QUANTUM SYSTEM DEMO:',
        'enter_alpha': 'Enter α value (real number):',
        'enter_beta': 'Enter β value (real number):',
        'apply_hadamard_question': 'Apply Hadamard gate? (y/n):',
        'error': '❌ Error',
        'ending_demo': '👋 Ending demonstration...',
        'invalid_choice': '❌ Invalid choice! Please enter a number between 1-4.',
        'superposition_not_possible': '❌ Superposition is not possible in classical systems!',
        'system_single_state': '   System can only exist in a single state.',
        'superposition_created_msg': '✅ Superposition created',
        'hadamard_gate_applied': '🔀 Hadamard gate applied',
        'new_state_vector': '   New state'
    }
}

# Varsayılan dil (Türkçe)
current_language = 'tr'

def set_language(lang: str):
    """Dil seçimi yapar / Sets the language"""
    global current_language
    if lang in LANGUAGES:
        current_language = lang
        print(f"🌐 Language set to: {lang.upper()}")
    else:
        print("❌ Invalid language! Using Turkish (tr)")

def get_text(key: str) -> str:
    """Seçili dilde metin döndürür / Returns text in selected language"""
    return LANGUAGES[current_language].get(key, key)

class ClassicalSystem:
    """Simulation of a classical system with deterministic behavior"""
    
    def __init__(self, initial_state: int = 0):
        """
        Initialize classical system
        
        Args:
            initial_state: Initial state of the system (0 or 1)
        """
        self.state = initial_state
        self.measurement_history = []
    
    def measure(self) -> int:
        """
        Measure the current state of the system
        
        Returns:
            Current state (0 or 1)
        """
        result = self.state
        self.measurement_history.append(result)
        return result
    
    def change_state(self, new_state: int):
        """
        Change the system state
        
        Args:
            new_state: New state (0 or 1)
        """
        if new_state in [0, 1]:
            self.state = new_state
        else:
            raise ValueError("State must be 0 or 1")
    
    def create_superposition(self):
        """Superposition is not possible in classical systems"""
        print(get_text('superposition_not_possible'))
        print(get_text('system_single_state'))
        return self.state

class QuantumSystem:
    """Simulation of a quantum system with probabilistic behavior"""
    
    def __init__(self, alpha: complex = 1.0, beta: complex = 0.0):
        """
        Initialize quantum system
        
        Args:
            alpha: Coefficient of |0⟩ state
            beta: Coefficient of |1⟩ state
        """
        # State vector: |ψ⟩ = α|0⟩ + β|1⟩
        self.alpha = alpha
        self.beta = beta
        self.measurement_history = []
        self._normalize()
    
    def _normalize(self):
        """Normalize the state vector (|α|² + |β|² = 1)"""
        norm = np.sqrt(abs(self.alpha)**2 + abs(self.beta)**2)
        if norm > 0:
            self.alpha /= norm
            self.beta /= norm
    
    def measure(self) -> int:
        """
        Measure the quantum system (Born rule)
        
        Returns:
            Measurement result (0 or 1)
        """
        # Born rule: P(0) = |α|², P(1) = |β|²
        p0 = abs(self.alpha)**2
        p1 = abs(self.beta)**2
        
        # Probabilistic measurement
        if random.random() < p0:
            result = 0
        else:
            result = 1
        
        self.measurement_history.append(result)
        return result
    
    def create_superposition(self, alpha: complex, beta: complex):
        """
        Create a superposition state
        
        Args:
            alpha: Coefficient of |0⟩ state
            beta: Coefficient of |1⟩ state
        """
        self.alpha = alpha
        self.beta = beta
        self._normalize()
        print(f"{get_text('superposition_created_msg')}: |ψ⟩ = {self.alpha:.3f}|0⟩ + {self.beta:.3f}|1⟩")
    
    def apply_hadamard(self):
        """Apply Hadamard gate (|0⟩ → |+⟩, |1⟩ → |-⟩)"""
        # Hadamard matrix: H = (1/√2) * [[1, 1], [1, -1]]
        new_alpha = (self.alpha + self.beta) / np.sqrt(2)
        new_beta = (self.alpha - self.beta) / np.sqrt(2)
        
        self.alpha = new_alpha
        self.beta = new_beta
        print(get_text('hadamard_gate_applied'))
        print(f"{get_text('new_state_vector')}: |ψ⟩ = {self.alpha:.3f}|0⟩ + {self.beta:.3f}|1⟩")

def classical_vs_quantum_demo():
    """Comparative demonstration of classical and quantum systems"""
    print("=" * 60)
    print(get_text('title'))
    print("=" * 60)
    
    # 1. Classical system demo
    print("\n" + get_text('classical_system'))
    classical = ClassicalSystem(initial_state=0)
    print(f"   {get_text('initial_state')}: {classical.state}")
    
    print("\n   " + get_text('measurements_deterministic') + ":")
    for i in range(5):
        result = classical.measure()
        print(f"   {get_text('measurement')} {i+1}: {result}")
    
    classical.change_state(1)
    print(f"\n   {get_text('state_changed')} {classical.state}")
    
    print("\n   " + get_text('measurements_after_change') + ":")
    for i in range(3):
        result = classical.measure()
        print(f"   {get_text('measurement')} {i+1}: {result}")
    
    # 2. Quantum system demo
    print("\n" + "=" * 60)
    print(get_text('quantum_system'))
    quantum = QuantumSystem(alpha=1.0, beta=0.0)
    print(f"   {get_text('initial_state')}: |ψ⟩ = |0⟩")
    
    print("\n   " + get_text('measurements_probabilistic') + ":")
    for i in range(5):
        result = quantum.measure()
        print(f"   {get_text('measurement')} {i+1}: {result}")
    
    # Create superposition
    print("\n   " + get_text('creating_superposition') + "...")
    quantum.create_superposition(1/np.sqrt(2), 1/np.sqrt(2))
    print(f"   |ψ⟩ = (1/√2)|0⟩ + (1/√2)|1⟩")
    print(f"   P(0) = |1/√2|² = 0.5, P(1) = |1/√2|² = 0.5")
    
    print("\n   " + get_text('measurements_in_superposition') + ":")
    for i in range(5):
        result = quantum.measure()
        print(f"   {get_text('measurement')} {i+1}: {result}")
    
    # Hadamard gate
    print("\n   " + get_text('applying_hadamard') + "...")
    quantum.apply_hadamard()
    
    print("\n   " + get_text('measurements_in_new_state') + ":")
    for i in range(3):
        result = quantum.measure()
        print(f"   {get_text('measurement')} {i+1}: {result}")

def state_evolution_plot():
    """Visualize the state evolution of classical and quantum systems"""
    print("\n" + get_text('drawing_plot'))
    
    # Classical system
    classical = ClassicalSystem(0)
    classical_measurements = []
    
    # State changes in classical system
    states = [0, 1, 0, 1, 0]
    for state in states:
        classical.change_state(state)
        classical_measurements.append(classical.measure())
    
    # Quantum system
    quantum = QuantumSystem(1.0, 0.0)
    quantum_measurements = []
    
    # Measurements in quantum system
    for i in range(len(states)):
        quantum_measurements.append(quantum.measure())
        if i == 2:  # Create superposition in the middle
            quantum.create_superposition(1/np.sqrt(2), 1/np.sqrt(2))
    
    # Plot creation
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    # Classical system
    ax1.plot(range(len(classical_measurements)), classical_measurements, 'bo-', linewidth=2, markersize=8)
    ax1.set_title(get_text('classical_title'), fontsize=14, fontweight='bold')
    ax1.set_ylabel(get_text('state'), fontsize=12)
    ax1.set_ylim(-0.5, 1.5)
    ax1.grid(True, alpha=0.3)
    ax1.set_xticks(range(len(classical_measurements)))
    ax1.set_xticklabels([f'{get_text("measurement")} {i+1}' for i in range(len(classical_measurements))])
    
    # Quantum system
    ax2.plot(range(len(quantum_measurements)), quantum_measurements, 'ro-', linewidth=2, markersize=8)
    ax2.set_title(get_text('quantum_title'), fontsize=14, fontweight='bold')
    ax2.set_xlabel(get_text('measurement_sequence'), fontsize=12)
    ax2.set_ylabel(get_text('state'), fontsize=12)
    ax2.set_ylim(-0.5, 1.5)
    ax2.grid(True, alpha=0.3)
    ax2.set_xticks(range(len(quantum_measurements)))
    ax2.set_xticklabels([f'{get_text("measurement")} {i+1}' for i in range(len(quantum_measurements))])
    
    plt.tight_layout()
    plt.show()

def interactive_demo():
    """Interactive demonstration with user input"""
    print("\n" + get_text('interactive_demo'))
    print("=" * 40)
    
    while True:
        print("\n" + get_text('options') + ":")
        print(f"{get_text('classical_demo')}")
        print(f"{get_text('quantum_demo')}")
        print(f"{get_text('state_evolution')}")
        print(f"{get_text('exit')}")
        
        choice = input("\n" + get_text('make_choice') + " ").strip()
        
        if choice == "1":
            print("\n" + get_text('classical_demo_title'))
            classical = ClassicalSystem(0)
            print(f"{get_text('initial_state')}: {classical.state}")
            
            for i in range(3):
                result = classical.measure()
                print(f"{get_text('measurement')} {i+1}: {result}")
            
            new_state = input(get_text('enter_new_state') + " ").strip()
            try:
                classical.change_state(int(new_state))
                print(f"{get_text('state_changed_to')}: {classical.state}")
            except ValueError:
                print(get_text('invalid_state'))
        
        elif choice == "2":
            print("\n" + get_text('quantum_demo_title'))
            alpha = float(input(get_text('enter_alpha') + " "))
            beta = float(input(get_text('enter_beta') + " "))
            
            try:
                quantum = QuantumSystem(alpha, beta)
                print(f"{get_text('state')}: |ψ⟩ = {quantum.alpha:.3f}|0⟩ + {quantum.beta:.3f}|1⟩")
                
                for i in range(3):
                    result = quantum.measure()
                    print(f"{get_text('measurement')} {i+1}: {result}")
                
                if input(get_text('apply_hadamard_question') + " ").lower() == 'y':
                    quantum.apply_hadamard()
                    
            except Exception as e:
                print(f"{get_text('error')}: {e}")
        
        elif choice == "3":
            state_evolution_plot()
        
        elif choice == "4":
            print(get_text('ending_demo'))
            break
        
        else:
            print(get_text('invalid_choice'))

def main():
    """Main function"""
    global current_language
    
    # Dil seçimi
    print("🌐 LANGUAGE SELECTION / DİL SEÇİMİ")
    print("=" * 50)
    print("1. Türkçe (Turkish)")
    print("2. English")
    print("=" * 50)
    
    lang_choice = input("Select language / Dil seçin (1-2): ").strip()
    if lang_choice == "2":
        set_language('en')
    else:
        set_language('tr')
    
    print("\n" + "=" * 50)
    if current_language == 'tr':
        print("🚀 KLASİK vs KUANTUM SİSTEMLER PROJESİ")
        print("Bu proje, klasik ve kuantum sistemlerin temel farklarını gösterir.")
        print("Öğreneceğiniz kavramlar:")
        print("• Deterministik vs Olasılıksal davranış")
        print("• Süperpozisyon durumları")
        print("• Kuantum ölçümü (Born kuralı)")
        print("• Hadamard kapısı")
    else:
        print("🚀 CLASSICAL vs QUANTUM SYSTEMS PROJECT")
        print("This project demonstrates the fundamental differences between classical and quantum systems.")
        print("Concepts you will learn:")
        print("• Deterministic vs Probabilistic behavior")
        print("• Superposition states")
        print("• Quantum measurement (Born rule)")
        print("• Hadamard gate")
    print("=" * 50)
    
    while True:
        if current_language == 'tr':
            print("\nSeçenekler:")
            print("1. Otomatik demo çalıştır")
            print("2. Durum evrimi grafiği")
            print("3. Etkileşimli demo")
            print("4. Çıkış")
            
            choice = input("\nSeçiminizi yapın (1-4): ").strip()
        else:
            print("\nOptions:")
            print("1. Run automatic demo")
            print("2. State evolution plot")
            print("3. Interactive demo")
            print("4. Exit")
            
            choice = input("\nMake your choice (1-4): ").strip()
        
        if choice == "1":
            classical_vs_quantum_demo()
        elif choice == "2":
            state_evolution_plot()
        elif choice == "3":
            interactive_demo()
        elif choice == "4":
            if current_language == 'tr':
                print("👋 Proje sonlandırılıyor...")
            else:
                print("👋 Ending project...")
            break
        else:
            if current_language == 'tr':
                print("❌ Geçersiz seçim! Lütfen 1-4 arası bir sayı girin.")
            else:
                print("❌ Invalid choice! Please enter a number between 1-4.")

if __name__ == "__main__":
    main()
