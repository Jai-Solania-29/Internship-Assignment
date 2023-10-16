FROM python:3.8-slim-buster

WORKDIR /app

RUN pip install Flask
RUN pip install psycopg2-binary

COPY . .

EXPOSE 8000

CMD ["python", "app.py"]
