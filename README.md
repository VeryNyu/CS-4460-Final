# CS-4460-Final

## Overview
Runs a small language model locally to simulate a social engineering hack.

## Requirements
- Python 3.x
- Ollama (https://ollama.com)

## Setup
1. Install Ollama
2. Run setup script:
   - Windows: `./setup.ps1`
   - Mac/Linux: `bash setup.sh`
3. The script will:
   - Create a virtual environment
   - Install dependencies
   - Pull the required model (`wizardlm2`)

## Run
```bash
python main.py
```

## Notes
- Ensure Ollama is running (ollama serve)
- First run may take time due to model download

## Troubleshooting
- Ollama not found → install and restart terminal
- Model issues → run ```ollama pull wizardlm2``` manually
- Permission issues (Mac/Linux) → ```chmod +x setup.sh```
