# Dockerfile
# Используйте официальный образ Python для работы
FROM python:3.11

# Установите рабочую директорию в контейнере
WORKDIR /app

# Копируйте файлы проекта в контейнер
COPY ./app /app

# Установите необходимые пакеты
RUN pip install -r requirements.txt

# Установите порт для веб-сервера
EXPOSE 8000

# Запустите сервер
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
