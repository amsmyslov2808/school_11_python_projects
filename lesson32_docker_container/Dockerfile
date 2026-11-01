# Берём компактный образ с Python.
FROM python:3.10.6-slim

# Все команды ниже выполняются в папке /app.
WORKDIR /app

# Зависимости копируем отдельно: Docker может переиспользовать слой их установки.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код бота и запускаем его.
COPY main.py .
COPY api.py .
# -u сразу выводит сообщения Python в логи контейнера, без буферизации.
CMD ["python", "-u", "main.py"]
