FROM python:3.7
WORKDIR /app
COPY . /app

RUN pip install -r /app/requirements.txt
ENV DATABASE_URL postgres://postgres:1234@db:5432/flask_db
EXPOSE 5000
#RUN python /app/init_db.py
CMD ["sh", "-c", "python init_db.py & python app.py"]

