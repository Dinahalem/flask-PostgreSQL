FROM python:3.7
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 9090
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=1234
ENV POSTGRES_HOST=*
ENV POSTGRES_DB=flask_db
#RUN python init_db.py
CMD ["sh", "-c", "python3 init_db.py && python app.py"]
