# Detektor Fraud AI

Platform AI Agent B2B untuk mendeteksi pola kecurangan finansial dalam data transaksi, dibangun dengan FastAPI dan Large Language Model (LLM).

## Latar Belakang Masalah

Startup fintech dan firma akuntansi memproses ribuan transaksi setiap hari. Audit manual tidak mungkin dilakukan dalam skala besar, dan sistem berbasis aturan tradisional melewatkan pola kecurangan canggih seperti:

- Split Invoicing: Memecah invoice besar menjadi beberapa invoice kecil untuk melewati batas persetujuan
- Cash Swiping: Penarikan tunai berulang dalam waktu singkat untuk menghindari deteksi ambang batas

## Solusi

API ini menggunakan AI Agent (berbasis LLM) sebagai Akuntan Forensik untuk menganalisis pola transaksi dan mendeteksi anomali dengan penalaran yang dapat dibaca manusia.

## Arsitektur

Klien/Web -> Backend FastAPI -> AI Agent (LLM) -> Router Multi-LLM (Claude, GPT, DeepSeek)

## Teknologi yang Digunakan

- Backend: Python 3.14, FastAPI, Uvicorn
- AI: OpenAI SDK (kompatibel dengan endpoint apapun yang mendukung OpenAI)
- Router LLM: Fallback multi-provider (Claude Sonnet, GPT, DeepSeek)
- Validasi Data: Pydantic v2

## Cara Menjalankan

### Prasyarat

- Python 3.11+
- Endpoint LLM (OpenAI, Anthropic, atau router yang kompatibel)

### Instalasi

    git clone https://github.com/kevinagustianawork/ai-fraud-detector.git
    cd ai-fraud-detector
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

### Jalankan Server

    uvicorn main:app --reload

Buka http://127.0.0.1:8000/docs untuk dokumentasi API interaktif.

## Endpoint API

### GET /

Health check - mengembalikan status API.

### GET /api/v1/audit-fraud

Menganalisis data transaksi simulasi dan mengembalikan kasus fraud yang terdeteksi.

Contoh Response:

    {
      "success": true,
      "data": {
        "has_fraud": true,
        "detected_cases": [
          {
            "case_type": "Split Invoicing",
            "suspect_user": "USR_02",
            "evidence_tx_ids": ["TX1002", "TX1003", "TX1004"],
            "reasoning_english": "User USR_02 memecah proyek renovasi kantor tunggal menjadi tiga invoice terpisah..."
          },
          {
            "case_type": "Cash Swiping",
            "suspect_user": "USR_03",
            "evidence_tx_ids": ["TX1005", "TX1006", "TX1007"],
            "reasoning_english": "User USR_03 melakukan tiga penarikan tunai identik..."
          }
        ]
      }
    }

## Kontrol Biaya dan Penanganan Error

- Output deterministik: temperature=0.1 dan response_format=json_object
- Fallback parsing: Mengekstrak JSON bahkan dari response LLM yang cacat
- Degradasi bertahap: Mengembalikan objek error terstruktur daripada crash

## Roadmap

- [ ] Dashboard frontend (React / Next.js)
- [ ] Generate laporan PDF
- [ ] Analisis streaming real-time
- [ ] Integrasi dengan API fintech nyata (Xendit, Midtrans)
- [ ] Model deteksi fraud yang di-fine-tune

## Lisensi

MIT License

## Penulis

Kevin Agustiana - Full-Stack AI Engineer

- GitHub: @kevinagustianawork
- LinkedIn: Kevin Agustiana

Star repositori ini jika bermanfaat!
