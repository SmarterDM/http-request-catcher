FROM python:3.6-alpine

WORKDIR /usr/src/app
ENV PYTHONPATH=/usr/src/app

COPY ./requirements.txt ./requirements.txt
COPY app.py .

RUN pip install --no-cache-dir -r requirements.txt && \
    chown 65534:65534 app.py && \
    chmod 400 app.py

EXPOSE 5000
USER nobody
ENTRYPOINT ["python", "app.py"]