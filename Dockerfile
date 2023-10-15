FROM python:3.8

WORKDIR /app

RUN pip install Flask

COPY . .

EXPOSE 8000

CMD ["python", "app.py"]
