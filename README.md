# 🎙 Speaker Backend (FastAPI + Azure TTS)

Backend service for story narration using Azure Speech (hi-IN-SwaraNeural).

---

## 🧱 Tech Stack

- FastAPI
- Uvicorn
- Azure Speech REST API
- Python 3.10+
- AWS Lightsail (Production)
- Nginx (Reverse Proxy)

---

# 🚀 Local Development Setup (NO .env)

## 1️⃣ Clone Repository

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

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Set Environment Variables (Local)

### Windows (PowerShell)

```powershell
$env:SPEECH_KEY="your_azure_key"
$env:SPEECH_REGION="centralindia"
```

### Mac / Linux

```bash
export SPEECH_KEY="your_azure_key"
export SPEECH_REGION="centralindia"
```

Verify:

```bash
echo $SPEECH_KEY
```

---

## 6️⃣ Run Backend (Development)

```bash
uvicorn main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

# 🏗 Production Deployment (AWS Lightsail)

## Systemd Service

File:

```
/etc/systemd/system/speaker-backend.service
```

```ini
[Unit]
Description=Speaker Backend FastAPI Service
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/speaker-backend
Environment="SPEECH_KEY=your_key"
Environment="SPEECH_REGION=centralindia"
ExecStart=/home/ubuntu/speaker-backend/venv/bin/uvicorn main:app --host 0.0.0.0 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
```

Enable service:

```bash
sudo systemctl daemon-reload
sudo systemctl start speaker-backend
sudo systemctl enable speaker-backend
```

---

# 🔄 Service Management

Restart:

```bash
sudo systemctl restart speaker-backend
```

Start:

```bash
sudo systemctl start speaker-backend
```

Stop:

```bash
sudo systemctl stop speaker-backend
```

Status:

```bash
sudo systemctl status speaker-backend
```

Reset failed state:

```bash
sudo systemctl reset-failed speaker-backend
```

---

# 📜 Logs

Live logs:

```bash
sudo journalctl -u speaker-backend -f
```

Last 100 lines:

```bash
sudo journalctl -u speaker-backend -n 100
```

---

# 🌐 Nginx Commands

Test config:

```bash
sudo nginx -t
```

Restart:

```bash
sudo systemctl restart nginx
```

Status:

```bash
sudo systemctl status nginx
```

Error logs:

```bash
sudo tail -f /var/log/nginx/error.log
```

---

# 🔐 SSL (Certbot)

Renew:

```bash
sudo certbot renew
```

List certificates:

```bash
sudo certbot certificates
```

---

# 📦 Deployment Workflow

```bash
cd ~/speaker-backend
git pull origin main
source venv/bin/activate
pip install -r requirements.txt
sudo systemctl restart speaker-backend
```

---

# 📦 Updating Dependencies

```bash
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Update dependencies"
git push
```

---

# 🎧 API Endpoint

## POST `/speak-chunk`

Request:

```json
{
  "text": "Hello world"
}
```

Response:

- `audio/mpeg`
- MP3 stream

---

# 👨‍💻 Author

Anshul Sharma