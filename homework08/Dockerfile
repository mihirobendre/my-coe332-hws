FROM python:3.10

# Set working directory
WORKDIR /app

COPY requirements.txt ./ 
RUN pip install -r requirements.txt

COPY routes.py worker.py jobs.py ./
ENV REDIS_IP 'redis-db'

CMD ["python3"]

