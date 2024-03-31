
# Analyzing NASA's Meteorite Landings Dataset

## Project Objective
This project aims to provide functions to analyze data from The HUGO Gene Nomenclature Committee's gene dataset. By processing and analyzing this data, researchers and enthusiasts can gain insights into the distribution and characteristics of gene data, contributing to our understanding of human genomes.

## Folder Contents
- `gene_api.py`: Contains the main /data and /gene routes for getting, posting and deleting data, as well as retreiving general and specific gene information.
- `Dockerfile`: Contains commands for creating container.
- `docker-compose.yml`: Contains instructions for composing the docker container, and starting/closing it.
- `requirements.txt`: Lists required packages and versions.

## Obtaining Data
- The dataset is sourced from HUGO Gene Nomenclature Committee's gene dataset. It does not need to be to be downloaded from their website, as it is pulled and parsed using the `requests` and `json` libraries.

# Running Tool in a Docker Container

Thank you for your interest in using our tool! This README will guide you through the process of setting up and running our tool in a Docker container from start to finish.

## Prerequisites
Before getting started, please ensure that you have the following installed on your system:
- Docker: Install Docker according to your operating system. You can find instructions on the [official Docker website](https://docs.docker.com/get-docker/).

## Steps to Run the Tool in a Docker Container

### 1. Clone the Repository
First, clone our repository to your local machine using the following command:

### 2. Build the Docker Image
Navigate to the directory where you cloned the repository, then build the Docker image using the provided Dockerfile. Run the following command:

This command will build a Docker image named `my-tool-image` based on the Dockerfile in the current directory.

### 3. Get Input Data
Our tool requires input data, which you can obtain from the web. Ensure that you have the necessary permissions and cite the data appropriately according to its license or terms of use.

### 4. Mount Data Inside the Container at Runtime
To provide input data to the container, you need to mount a volume when running the container. Replace `/path/to/local/data` with the path to the directory containing your input data, and `/path/to/container/data` with the path where you want to mount the data inside the container. Run the container using the following command:

### 5. Run the Containerized Code
Once the container is running, the tool will be executed automatically using the input data provided. Sit back and let the tool do its magic!

### 6. Run the Containerized Unit Tests
We have included unit tests to ensure the functionality of our tool. To run the unit tests within the Docker container, you can execute the following command:

This command will run the unit tests using the pytest framework inside the container.

## Additional Notes
- If you encounter any issues or have questions, please refer to our documentation or reach out to our support team.
- Make sure to clean up any resources (containers, images) when you're finished by using `docker rm` and `docker rmi` commands.

Thank you for using our tool! We hope you find it useful. If you have any feedback or suggestions, we'd love to hear from you. Happy analyzing!


## Running the Code on your system
1. Ensure Python 3 is installed on your system.
2. Open a terminal or command prompt and navigate to the directory containing the scripts.
3. Run the script `ml_data_analysis.py` using the Python interpreter: `python3 ml_data_analysis.py`.
4. Interpret the results by observing the cleaned data, summary statistics, or computed distances printed in the terminal.


Generated using the help of ChatGPT

