FROM python:3.12-slim

COPY . .

RUN pip install -r app/requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]