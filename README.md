# AI Çeviri 

Bu proje, Google'ın Gemini AI modelini kullanarak çeviri uygulaması.

## Özellikler

- Çeviri API'si (Port 8000)
- Google Gemini AI entegrasyonu
- FastAPI ile modern API tasarımı

## Kurulum

1. Projeyi klonlayın:
```bash
git clone https://github.com/kullaniciadi/proje-adi.git
cd proje-adi
```

2. Sanal ortam oluşturun ve aktifleştirin:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac için
venv\Scripts\activate     # Windows için
```

3. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

4. `.env` dosyası oluşturun ve Google API anahtarınızı ekleyin:
```
GOOGLE_API_KEY=your_api_key_here
```

## Kullanım

1. Çeviri API'sini başlatın:
```bash
python at.py
```

### Çeviri API Örneği
```bash
curl -X POST http://localhost:8000/translate -H "Content-Type: application/json" -d '{"text": "Hello world", "language": "Türkçe"}'
```
