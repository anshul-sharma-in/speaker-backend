# 🎙 Speaker Backend (FastAPI + Azure Swara Neural)

Backend service for story narration using Azure Cognitive Services Speech (hi-IN-SwaraNeural).

---

## 🧱 Tech Stack

- FastAPI
- Uvicorn
- Azure Cognitive Services (Speech)
- Python 3.10+
- AWS Lightsail (Production)

---

# 🚀 Local Development Setup

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/speaker-backend.git
cd speaker-backend
```

---

## 2️⃣ Create Virtual Environment (First Time Only)

```bash
python -m venv venv
```

---

## 3️⃣ Activate Virtual Environment

### Windows (PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

### Mac / Linux

```bash
source venv/bin/activate
```

You should see:

```
(venv)
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Create `.env` File

Create a file named `.env` in project root:

```
SPEECH_KEY=your_azure_key
SPEECH_REGION=centralindia
```

⚠ Never commit this file.

---

## 6️⃣ Run Backend (Development Mode)

```bash
uvicorn main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

# 🏗 Production Deployment (AWS Lightsail)

## Manual Run

```bash
source venv/bin/activate
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Systemd Service (Recommended)

Create:

```
/etc/systemd/system/swara.service
```

Example:

```ini
[Unit]
Description=Swara FastAPI Service
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/speaker-backend
ExecStart=/home/ubuntu/speaker-backend/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable:

```bash
sudo systemctl daemon-reload
sudo systemctl start swara
sudo systemctl enable swara
```

---

# 📦 Updating Dependencies

After installing a new package:

```bash
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Update dependencies"
git push
```

---

# 🔐 Environment Variables

Ensure `.gitignore` contains:

```
.env
venv/
__pycache__/
*.pyc
```

---

# 🎧 API Endpoint

## POST `/speak-chunk`

### Request Body

```json
{
  "text": "Hello world"
}
```

### Response

- `audio/mpeg`
- Returns MP3 audio stream

---

# 🧠 Development Commands Cheat Sheet

```bash
cd speaker-backend
.\venv\Scripts\Activate.ps1   # Windows
source venv/bin/activate      # Mac/Linux
uvicorn main:app --reload
```

---

# 👨‍💻 Author

Anshul Sharma