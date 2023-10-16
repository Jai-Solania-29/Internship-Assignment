FROM python:3.8-slim-buster

WORKDIR /app

RUN pip install Flask

COPY . .

EXPOSE 8000

CMD ["python", "app.py"]
