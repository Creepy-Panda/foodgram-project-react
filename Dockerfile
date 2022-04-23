FROM python:3.7-slim

WORKDIR /app

COPY backend/requirements.txt .

COPY backend/ /app

RUN pip3 install -r requirements.txt

COPY . .

CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000"] 