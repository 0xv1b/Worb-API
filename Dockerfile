FROM python:3.10

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD [ "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
