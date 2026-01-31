#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BASE_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"

LOG_DIR="$BASE_DIR/bash/logs"
LOG_ARQ="$LOG_DIR/logs_email_monitoring.txt"
DATE=$(date +"%Y-%m-%d %H:%M:%S")

mkdir -p "$LOG_DIR"
python3 "$BASE_DIR/send_email.py"

STATUS=$? # Espera retorno da função python informando se teve sucesso ou não ao enviar o e-mail

if [ $STATUS -eq 0 ]; then
    echo "[$DATE] INFO: Processo executado com sucesso" >> "$LOG_ARQ"
else
    echo "[$DATE] ERROR: Falha ao executar o processo (API fora ou erro interno)" >> "$LOG_ARQ"
fi
