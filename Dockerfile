FROM python:3.9-slim

WORKDIR /webapp

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=/webapp/site.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
