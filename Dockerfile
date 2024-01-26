FROM python:3.11-slim

WORKDIR /code

COPY ./requirements.txt /code

COPY ./main.py /code

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5555"]
