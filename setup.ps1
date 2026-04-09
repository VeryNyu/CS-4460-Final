Write-Host "== Creating virtual environment =="
if (!(Test-Path "venv")) {
    python -m venv venv
}

Write-Host "== Activating =="
.\venv\Scripts\activate

Write-Host "== Installing dependencies =="
pip install --upgrade pip
pip install -r requirements.txt

Write-Host "== Checking Ollama =="
if (!(Get-Command ollama -ErrorAction SilentlyContinue)) {
    Write-Host "Install Ollama manually from https://ollama.com"
} else {
    Write-Host "Ollama already installed."
}

Write-Host "== Pulling model =="
ollama pull wizardlm2

Write-Host "== Done! Run: python main.py =="
