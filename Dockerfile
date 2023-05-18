FROM python:3.7
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 9090
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=
ENV POSTGRES_HOST=localhost
ENV POSTGRES_DB=flask_db
CMD ["python","app.py"]
