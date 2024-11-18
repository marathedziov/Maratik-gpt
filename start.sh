#!/bin/bash

# Exit early on errors
set -eu

# Python buffers stdout. Without this, you won't see what you "print" in the Activity Logs
export PYTHONUNBUFFERED=true

# Устанавливаем pip, если его нет
if ! command -v pip &> /dev/null
then
    echo "pip not found. Installing..."
    curl --silent --show-error --retry 5 https://bootstrap.pypa.io/pip/3.7/get-pip.py | python3
fi

# Устанавливаем зависимости из requirements.txt
pip install --no-cache-dir -r requirements.txt

# Запускаем бота
python bot.py
