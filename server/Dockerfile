FROM python:3.11

WORKDIR /server

COPY ./server /server
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "5000", "--reload"]
