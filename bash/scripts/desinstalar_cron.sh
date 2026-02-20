#!/bin/bash

DIR="$(cd "$(dirname "$0")" && pwd)"
crontab -l 2>/dev/null | grep -vF "$DIR/email_monitoring.sh" | crontab -
echo "Cron removido com sucesso!"