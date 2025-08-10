# Classical vs Quantum Systems Simulation / Klasik vs Kuantum Sistemler Simülasyonu

[🇹🇷 Türkçe](#türkçe) | [🇺🇸 English](#english)

---

## 🇹🇷 Türkçe

### 📋 Proje Genel Bakışı

Bu proje, klasik ve kuantum hesaplama sistemleri arasındaki temel farkları interaktif simülasyonlar ve görselleştirmeler aracılığıyla gösteren kapsamlı bir Python projesidir.

**Çok dilli destek: 🇹🇷 Türkçe | 🇺🇸 English**

### 🎯 Proje Amacı

Bu proje şunlarla ilgili pratik deneyim sağlar:
- **Klasik Sistemler**: Kesin sonuçlarla deterministik davranış
- **Kuantum Sistemler**: Süperpozisyon durumlarıyla olasılıksal davranış
- **Kuantum Kapıları**: Hadamard kapısının uygulanması
- **Ölçüm Teorisi**: Born kuralı ve kuantum ölçüm çökmesi

### 🚀 Özellikler

#### 🌐 Çok Dilli Destek
- **Türkçe**: Tam Türkçe arayüz ve açıklamalar
- **İngilizce**: Tam İngilizce arayüz ve dokümantasyon
- **Dil Seçimi**: Başlangıçta tercih ettiğiniz dili seçin

#### Temel Bileşenler
- **ClassicalSystem Sınıfı**: Klasik ikili sistemleri simüle eder
- **QuantumSystem Sınıfı**: Kuantum kubit davranışını uygular
- **İnteraktif Demolar**: Her iki sistemin de pratik keşfi
- **Görselleştirme Araçları**: matplotlib kullanarak durum evrim grafikleri

#### Gösterilen Anahtar Kavramlar
- Kuantum sistemlerde süperpozisyon durumları
- Deterministik vs olasılıksal ölçüm
- Hadamard kapısı dönüşümleri
- Durum vektörü normalizasyonu
- Kuantum ölçüm çökmesi

### 📋 Gereksinimler

```bash
pip install -r requirements.txt
```

**Bağımlılıklar:**
- `numpy==1.24.3` - Sayısal hesaplamalar
- `matplotlib==3.7.1` - Veri görselleştirme

### 🏃‍♂️ Hızlı Başlangıç

1. **Depoyu klonlayın:**
   ```bash
   git clone <your-repo-url>
   cd quantum_simulation_project
   ```

2. **Bağımlılıkları yükleyin:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Projeyi çalıştırın:**
   ```bash
   python Quantum_simulation_project.py
   ```

4. **Dilinizi seçin:**
   - **1**: Türkçe
   - **2**: English

### 🎮 Kullanım

#### Ana Menü Seçenekleri

1. **Otomatik Demo**: Her iki sistemin kapsamlı gösterimi
2. **Durum Evrim Grafiği**: Klasik vs kuantum davranışının görsel karşılaştırması
3. **İnteraktif Demo**: Özel parametrelerle pratik keşif
4. **Çıkış**: Uygulamayı kapat

#### İnteraktif Özellikler

- **Klasik Sistem Demo**: Durumları değiştirin ve deterministik davranışı gözlemleyin
- **Kuantum Sistem Demo**: Süperpozisyon durumları oluşturun ve kuantum kapıları uygulayın
- **Parametre Girişi**: Kuantum durumları için α ve β değerlerini özelleştirin
- **Gerçek Zamanlı Görselleştirme**: Ölçüm sonuçlarını ve durum değişikliklerini görün

### 🔬 Teknik Detaylar

#### Klasik Sistem
- İkili durum temsili (0 veya 1)
- Deterministik durum geçişleri
- Süperpozisyon yeteneği yok
- Anında ölçüm sonuçları

#### Kuantum Sistem
- Karmaşık durum vektörü: |ψ⟩ = α|0⟩ + β|1⟩
- Süperpozisyon durumları
- Olasılıksal ölçüm (Born kuralı)
- Durum vektörü normalizasyonu
- Hadamard kapısı uygulaması

#### Hadamard Kapısı
Hadamard kapısı kuantum durumlarını dönüştürür:
- |0⟩ → |+⟩ = (1/√2)(|0⟩ + |1⟩)
- |1⟩ → |-⟩ = (1/√2)(|0⟩ - |1⟩)

Matris temsili:
```
H = (1/√2) × [[1,  1]
                [1, -1]]
```

### 📊 Örnek Çıktı

```
🔬 KLASİK vs KUANTUM SİSTEMLER GÖSTERİMİ
============================================================

📊 1. KLASİK SİSTEM:
   Başlangıç durumu: 0

   Ölçümler (deterministik):
   Ölçüm 1: 0
   Ölçüm 2: 0
   Ölçüm 3: 0
   Ölçüm 4: 0
   Ölçüm 5: 0

⚛️ 2. KUANTUM SİSTEM:
   Başlangıç durumu: |ψ⟩ = |0⟩

   Ölçümler (olasılıksal):
   Ölçüm 1: 0
   Ölçüm 2: 0
   Ölçüm 3: 1
   Ölçüm 4: 0
   Ölçüm 5: 1

   Süperpozisyon oluşturuluyor...
   ✅ Süperpozisyon oluşturuldu: |ψ⟩ = 0.707|0⟩ + 0.707|1⟩
```

### 🧪 Öğrenme Hedefleri

Bu projeyi tamamladıktan sonra şunları anlayacaksınız:

1. **Temel Farklar**: Klasik ve kuantum sistemlerin nasıl farklı davrandığı
2. **Süperpozisyon**: Bir kuantum sistemin birden fazla durumda var olmasının ne anlama geldiği
3. **Ölçüm**: Kuantum ölçümünün sistem durumlarını nasıl etkilediği
4. **Kuantum Kapıları**: Temel kuantum işlemleri ve etkileri
5. **Olasılık**: Olasılığın kuantum mekaniğindeki rolü

### 🔍 Kod Yapısı

```
├── Quantum_simulation_project.py    # Ana proje dosyası
├── requirements.txt            # Python bağımlılıkları
└── README.md                  # Proje dokümantasyonu
```

#### Anahtar Sınıflar ve Metodlar

- **ClassicalSystem**: `__init__()`, `measure()`, `change_state()`
- **QuantumSystem**: `__init__()`, `measure()`, `create_superposition()`, `apply_hadamard()`
- **Yardımcı Fonksiyonlar**: `classical_vs_quantum_demo()`, `state_evolution_plot()`, `interactive_demo()`

### 🤝 Katkıda Bulunma

Katkılarınız memnuniyetle karşılanır! Lütfen bir Pull Request göndermekten çekinmeyin.

#### Geliştirme Kuralları
- PEP 8 stil kurallarını takip edin
- Kapsamlı docstring'ler ekleyin
- Yeni özellikler için unit testler dahil edin
- Gerektiğinde dokümantasyonu güncelleyin

### 📚 Daha Fazla Okuma

- [Bilgisayar Bilimcileri için Kuantum Hesaplama](https://www.cambridge.org/core/books/quantum-computing-for-computer-scientists/)
- [Qiskit Dokümantasyonu](https://qiskit.org/documentation/)
- [Kuantum Mekaniği Kavramları](https://tr.wikipedia.org/wiki/Kuantum_mekaniği)

### 📄 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır - detaylar için [LICENSE](LICENSE) dosyasına bakın.

### 👨‍💻 Yazar

Semih - [semihkulekcioglu@gmail.com]

---

## 🇺🇸 English

### 📋 Project Overview

A comprehensive Python project that demonstrates the fundamental differences between classical and quantum computing systems through interactive simulations and visualizations.

**Multi-language support: 🇹🇷 Türkçe | 🇺🇸 English**

### 🎯 Project Purpose

This project provides hands-on experience with:
- **Classical Systems**: Deterministic behavior with definite outcomes
- **Quantum Systems**: Probabilistic behavior with superposition states
- **Quantum Gates**: Implementation of the Hadamard gate
- **Measurement Theory**: Born rule and quantum measurement collapse

### 🚀 Features

#### 🌐 Multi-Language Support
- **Turkish (Türkçe)**: Full Turkish interface and explanations
- **English**: Complete English interface and documentation
- **Language Selection**: Choose your preferred language at startup

#### Core Components
- **ClassicalSystem Class**: Simulates classical binary systems
- **QuantumSystem Class**: Implements quantum qubit behavior
- **Interactive Demos**: Hands-on exploration of both systems
- **Visualization Tools**: State evolution plots using matplotlib

#### Key Concepts Demonstrated
- Superposition states in quantum systems
- Deterministic vs probabilistic measurement
- Hadamard gate transformations
- State vector normalization
- Quantum measurement collapse

### 📋 Requirements

```bash
pip install -r requirements.txt
```

**Dependencies:**
- `numpy==1.24.3` - Numerical computations
- `matplotlib==3.7.1` - Data visualization

### 🏃‍♂️ Quick Start

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd quantum-simulation-project
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the project:**
   ```bash
   python Quantum_simulation_project.py
   ```

4. **Choose your language:**
   - **1**: Türkçe (Turkish)
   - **2**: English

### 🎮 Usage

#### Main Menu Options

1. **Automatic Demo**: Comprehensive demonstration of both systems
2. **State Evolution Plot**: Visual comparison of classical vs quantum behavior
3. **Interactive Demo**: Hands-on exploration with custom parameters
4. **Exit**: Close the application

#### Interactive Features

- **Classical System Demo**: Change states and observe deterministic behavior
- **Quantum System Demo**: Create superposition states and apply quantum gates
- **Parameter Input**: Customize α and β values for quantum states
- **Real-time Visualization**: See measurement results and state changes

### 🔬 Technical Details

#### Classical System
- Binary state representation (0 or 1)
- Deterministic state transitions
- No superposition capability
- Immediate measurement results

#### Quantum System
- Complex state vector: |ψ⟩ = α|0⟩ + β|1⟩
- Superposition states
- Probabilistic measurement (Born rule)
- State vector normalization
- Hadamard gate implementation

#### Hadamard Gate
The Hadamard gate transforms quantum states:
- |0⟩ → |+⟩ = (1/√2)(|0⟩ + |1⟩)
- |1⟩ → |-⟩ = (1/√2)(|0⟩ - |1⟩)

Matrix representation:
```
H = (1/√2) × [[1,  1]
                [1, -1]]
```

### 📊 Example Output

```
🔬 CLASSICAL vs QUANTUM SYSTEMS DEMONSTRATION
============================================================

📊 1. CLASSICAL SYSTEM:
   Initial state: 0

   Measurements (deterministic):
   Measurement 1: 0
   Measurement 2: 0
   Measurement 3: 0
   Measurement 4: 0
   Measurement 5: 0

⚛️ 2. QUANTUM SYSTEM:
   Initial state: |ψ⟩ = |0⟩

   Measurements (probabilistic):
   Measurement 1: 0
   Measurement 2: 0
   Measurement 3: 1
   Measurement 4: 0
   Measurement 5: 1

   Creating superposition...
   ✅ Superposition created: |ψ⟩ = 0.707|0⟩ + 0.707|1⟩
```

### 🧪 Learning Objectives

After completing this project, you will understand:

1. **Fundamental Differences**: How classical and quantum systems behave differently
2. **Superposition**: What it means for a quantum system to exist in multiple states
3. **Measurement**: How quantum measurement affects system states
4. **Quantum Gates**: Basic quantum operations and their effects
5. **Probability**: The role of probability in quantum mechanics

### 🔍 Code Structure

```
├── Quantum_simulation_project.py    # Main project file
├── requirements.txt            # Python dependencies
└── README.md                  # Project documentation
```

#### Key Classes and Methods

- **ClassicalSystem**: `__init__()`, `measure()`, `change_state()`
- **QuantumSystem**: `__init__()`, `measure()`, `create_superposition()`, `apply_hadamard()`
- **Utility Functions**: `classical_vs_quantum_demo()`, `state_evolution_plot()`, `interactive_demo()`

### 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

#### Development Guidelines
- Follow PEP 8 style guidelines
- Add comprehensive docstrings
- Include unit tests for new features
- Update documentation as needed

### 📚 Further Reading

- [Quantum Computing for Computer Scientists](https://www.cambridge.org/core/books/quantum-computing-for-computer-scientists/)
- [Qiskit Documentation](https://qiskit.org/documentation/)
- [Quantum Mechanics Concepts](https://en.wikipedia.org/wiki/Quantum_mechanics)

### 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### 👨‍💻 Author

Semih - [semihkulekcioglu@gmail.com]

---

**Note / Not**: This project is designed for educational purposes and serves as a foundation for understanding quantum computing principles. For production quantum computing applications, consider using established frameworks like Qiskit or Cirq.

**Not**: Bu proje eğitim amaçlı tasarlanmıştır ve kuantum hesaplama prensiplerini anlamak için temel oluşturur. Üretim kuantum hesaplama uygulamaları için Qiskit veya Cirq gibi kurulmuş çerçeveleri kullanmayı düşünün.
