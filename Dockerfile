FROM python:3.6-alpine

WORKDIR /usr/src/app
ENV PYTHONPATH=/usr/src/app

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
