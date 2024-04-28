FROM python:3.10

# Set working directory
WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY api.py worker.py jobs.py ./

CMD ["python3"]

