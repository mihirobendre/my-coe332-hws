FROM python:3.10.12

# Create /app directory
RUN mkdir /app

# Set working directory
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY flask_app.py /app/flask_app.py
CMD ["python3", "/app/flask_app.py"]

