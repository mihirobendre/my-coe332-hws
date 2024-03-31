
# Analyzing HUGO Gene Nomenclature Committee dataset

## Project Objective
This project aims to provide functions to analyze data from The HUGO Gene Nomenclature Committee's gene dataset. By processing and analyzing this data, researchers and enthusiasts can gain insights into the distribution and characteristics of gene data, contributing to our understanding of human genomes.

## Folder Contents
- `gene_api.py`: Contains the main /data and /gene routes for getting, posting and deleting data, as well as retreiving general and specific gene information.
- `Dockerfile`: Contains commands for creating container.
- `docker-compose.yml`: Contains instructions for composing the docker container, and starting/closing it.
- `requirements.txt`: Lists required packages and versions.

## Obtaining Data
- The dataset is sourced from HUGO Gene Nomenclature Committee's gene dataset. It does not need to be to be downloaded from their website, as it is pulled and parsed using the `requests` and `json` libraries.

## Instructions to build a new image from your Dockerfile
- Build a docker image from your Dockerfile: `docker build -t gene_api .`
- Run the docker app: `docker run --rm -u $(id -u):$(id -g) -p 6379:6379 -d -v $PWD/data:/data redis:7 --save 1 1`
- Transfer ownership of data folder from root to ubuntu: `sudo chown ubuntu:ubuntu data/`

## Instructions to launch the containerized app and Redis using docker-compose
- `docker-compose up -d --build`: to start running the docker container (flask app + redis)
- `docker-compose down`: to stop docker container

## Example API query commands and expected outputs in code blocks
- `curl localhost:5000/`: Outputs "Hello, world!"
- `curl localhost:5000/data`: Outputs currently loaded data in database (initially, this should be empty "[]")
- `curl -X GET localhost:5000/data`: Outputs currently loaded data in database (initially, this should be empty "[]")
- `curl -X POST localhost:5000/data`: Posts HGNC data to redis database
- `curl -X DELETE localhost:5000/data`: Deletes all data in database
- `curl localhost:5000/gene`: Returns list of all `hgnc_id`'s
- `curl localhost:5000/gene/<hgnc_id>`: Returns all info for the specific `hgnc_id`, e.x. for HGNC:37 it returns:

`{"ucsc_id": "uc002lqw.5", "locus_group": "protein-coding gene", "ena": ["AF328787"], "mgd_id": ["MGI:1351646"], "symbol": "ABCA7", "locus_type": "gene with protein product", "name": "ATP binding cassette subfamily A member 7", "rgd_id": ["RGD:1303134"], "iuphar": "objectId:762", "prev_name": ["ATP-binding cassette, sub-family A (ABC1), member 7"], "gencc": "HGNC:37", "pubmed_id": [10873640, 11435699, 12917409], "mane_select": ["ENST00000263094.11", "NM_019112.4"], "gene_group_id": [805], "alias_symbol": ["ABCX"], "gene_group": ["ATP binding cassette subfamily A"], "_version_": 1794565469998415872, "vega_id": "OTTHUMG00000167547", "entrez_id": "10347", "uuid": "fafebd35-466b-4317-91a7-b5f4db4797fa", "date_name_changed": "2015-11-13", "location_sortable": "19p13.3", "location": "19p13.3", "status": "Approved", "ccds_id": ["CCDS12055"], "date_approved_reserved": "1999-06-11", "date_modified": "2023-01-20", "uniprot_ids": ["Q8IZY2"], "omim_id": ["605414"], "agr": "HGNC:37", "refseq_accession": ["NM_019112"], "ensembl_gene_id": "ENSG00000064687", "hgnc_id": "HGNC:37"}`


## Prerequisites
Before getting started, please ensure that you have the following installed on your system:
- Docker: Install Docker according to your operating system. You can find instructions on the [official Docker website](https://docs.docker.com/get-docker/).


