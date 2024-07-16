FROM python:3.11-slim

WORKDIR /work

COPY . .

RUN pip install --upgrade pip --no-cache-dir
RUN pip install -r requirements.txt --no-cache-dir

CMD ["gunicorn", "main:app", "-b", "0.0.0.0:5000"]