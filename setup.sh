#!/usr/bin/env bash
set -euo pipefail

step() {
  echo -e "\n== $1 =="
}

VENV_DIR="venv"
ACTIVATE_SCRIPT="$VENV_DIR/Scripts/activate"

step "Checking Python"
if ! command -v python3 >/dev/null 2>&1; then
  echo "Python3 is required but not installed."
  exit 1
fi

step "Creating virtual environment"
if [ ! -d "$VENV_DIR" ]; then
  python3 -m venv "$VENV_DIR"
else
  echo "Virtual environment already exists."
fi

step "Activating virtual environment"
if [ ! -f "$ACTIVATE_SCRIPT" ]; then
  echo "Activation script not found: $ACTIVATE_SCRIPT"
  exit 1
fi
# shellcheck disable=SC1090
source "$ACTIVATE_SCRIPT"

step "Installing dependencies"
python -m pip install --upgrade pip
pip install -r requirements.txt

step "Checking Ollama"
if ! command -v ollama >/dev/null 2>&1; then
  echo "Installing Ollama..."
  curl -fsSL https://ollama.com/install.sh | sh
else
  echo "Ollama already installed."
fi

step "Ensuring Ollama is running"
if ! pgrep -x "ollama" >/dev/null 2>&1; then
  ollama serve >/dev/null 2>&1 &
  sleep 3
  echo "Ollama started."
else
  echo "Ollama already running."
fi

step "Pulling model"
ollama pull wizardlm2

step "Setup complete"
echo "Run:"
echo "source $ACTIVATE_SCRIPT && python main.py"
