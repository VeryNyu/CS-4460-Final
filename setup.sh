#!/bin/bash

set -e

echo "== Checking Python =="
if ! command -v python3 &> /dev/null
then
    echo "Python3 is required but not installed."
    exit 1
fi

echo "== Creating virtual environment =="
if [ ! -d "venv" ]; then
    python3 -m venv venv
else
    echo "venv already exists, skipping..."
fi

echo "== Activating virtual environment =="
source venv/bin/activate

echo "== Installing dependencies =="
pip install --upgrade pip
pip install -r requirements.txt

echo "== Checking Ollama =="
if ! command -v ollama &> /dev/null
then
    echo "Installing Ollama..."
    curl -fsSL https://ollama.com/install.sh | sh
else
    echo "Ollama already installed."
fi

echo "== Ensuring Ollama is running =="
if ! pgrep -x "ollama" > /dev/null
then
    ollama serve > /dev/null 2>&1 &
    sleep 3
    echo "Ollama started."
else
    echo "Ollama already running."
fi

echo "== Pulling model (if needed) =="
ollama pull llama3

echo "== Setup complete =="
echo "Activate env and run:"
echo "source venv/bin/activate && python main.py"
