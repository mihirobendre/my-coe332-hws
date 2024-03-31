FROM python:3.10.12

# Create /app directory
RUN mkdir /app

# Set working directory
WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY gene_api.py /app/gene_api.py
CMD ["python3", "/app/gene_api.py"]

