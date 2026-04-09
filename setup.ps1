$ErrorActionPreference = "Stop"

function Step($msg) {
    Write-Host "`n== $msg ==" -ForegroundColor Cyan
}

# Paths
$venvPath = "venv"
$activateScript = "$venvPath\Scripts\Activate.ps1"

Step "Creating virtual environment"
if (-not (Test-Path $venvPath)) {
    python -m venv $venvPath
} else {
    Write-Host "Virtual environment already exists."
}

Step "Activating virtual environment"
if (-not (Test-Path $activateScript)) {
    throw "Activation script not found: $activateScript"
}
& $activateScript

Step "Installing dependencies"
python -m pip install --upgrade pip
pip install -r requirements.txt

Step "Checking Ollama"
$ollamaExists = Get-Command ollama -ErrorAction SilentlyContinue

if (-not $ollamaExists) {
    Write-Warning "Ollama not found. Install it from https://ollama.com"
} else {
    Write-Host "Ollama is installed."

    Step "Pulling model"
    ollama pull wizardlm2
}

Step "Done"
Write-Host "Run: python main.py" -ForegroundColor Green