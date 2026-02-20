#!/bin/bash

# Pega o diretório onde o script está localizado (caminho absoluto)
DIR="$(cd "$(dirname "$0")" && pwd)"

#Torna o script de monitoramento de e-mails executável, caso não esteja
chmod +x "$DIR/email_monitoring.sh"

echo "$DIR/email_monitoring.sh"

# Define o comando cron usando o caminho dinâmico
HORA="*"
MINUTO="*" # minuto em minuto
CRON_JOB="$MINUTO $HORA * * * /bin/bash $DIR/email_monitoring.sh"

# Verifica se o cron já existe para não duplicar
(crontab -l 2>/dev/null | grep -qF "$DIR/email_monitoring.sh") && {
    echo "Cron já instalado. Nada foi alterado."
    exit 0
}

# Adiciona o cron
(crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -

echo "Cron instalado com sucesso!"
echo "Comando registrado: $CRON_JOB"