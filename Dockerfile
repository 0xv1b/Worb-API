FROM python:3.10

COPY ./src /app/src

WORKDIR /app

RUN pip install uvicorn pydantic fastapi redis 

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host=0.0.0.0", "--reload"]