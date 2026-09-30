# Берём компактный образ с Python.
FROM python:3.10.6-slim

# Все команды ниже выполняются в папке /app.
WORKDIR /app

# Устанавливаем библиотеки для бота.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код бота и запускаем его.
COPY main.py .
CMD ["python", "-u", "main.py"]
