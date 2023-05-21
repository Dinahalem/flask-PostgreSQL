FROM python:3.7
WORKDIR /app
COPY . /app

RUN pip install -r /app/requirements.txt
EXPOSE 5000
#RUN python /app/init_db.py
#CMD ["sh", "-c", "python /docker-entrypoint-initdb.d/init_db.py && /app/app.py"]

