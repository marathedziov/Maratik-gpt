#!/bin/bash

# Exit early on errors
set -eu

# Python buffers stdout. Without this, you won't see what you "print" in the Activity Logs
export PYTHONUNBUFFERED=true

# Install Python 3 virtual env
VIRTUALENV=./venv

# Создаем виртуальное окружение, если его нет
if [ ! -d $VIRTUALENV ]; then
  python3 -m venv $VIRTUALENV
fi

# Активируем виртуальное окружение
source $VIRTUALENV/bin/activate

# Устанавливаем pip, если его нет в виртуальном окружении
if [ ! -f $VIRTUALENV/bin/pip ]; then
  curl --silent --show-error --retry 5 https://bootstrap.pypa.io/pip/3.7/get-pip.py | python3
fi

# Устанавливаем зависимости из requirements.txt
pip install --no-cache-dir -r requirements.txt

# Запускаем бота
python bot.py
