FROM python:3.7
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 9090
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=1234
ENV POSTGRES_HOST=localhost
ENV POSTGRES_DB=flask_db
ENTRYPOINT ["python3","init_db.py"]
Entrypoint ["python3","app.py"]
