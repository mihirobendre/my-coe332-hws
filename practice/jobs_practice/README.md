
# Analyzing HUGO Gene Nomenclature Committee dataset

## Project Objective
This project aims to provide functions to analyze data from The HUGO Gene Nomenclature Committee's gene dataset. By processing and analyzing this data, researchers and enthusiasts can gain insights into the distribution and characteristics of gene data, contributing to our understanding of human genomes.

## Folder Contents
- `gene_api.py`: Contains the main /data and /gene routes for getting, posting and deleting data, as well as retreiving general and specific gene information.
- `Dockerfile`: Contains commands for creating container.
- `docker-compose.yml`: Contains instructions for composing the docker container, and starting/closing it.
- `requirements.txt`: Lists required packages and versions.

## Description of Data

The [Human Genome Nomenclature Committee (HGNC) dataset](https://www.genenames.org/download/archive/) (citation below) provides comprehensive information about human genes approved by the HGNC. Each entry in the dataset corresponds to a unique gene and contains various attributes describing its properties and associations. Here's a description of the columns included in the dataset:

| Column Name              | Description                                                                                         |
|--------------------------|-----------------------------------------------------------------------------------------------------|
| hgnc_id                  | HGNC ID. A unique ID created by the HGNC for every approved symbol.                                 |
| symbol                   | The HGNC approved gene symbol. Equates to the "APPROVED SYMBOL" field within the gene symbol report. |
| name                     | HGNC approved name for the gene. Equates to the "APPROVED NAME" field within the gene symbol report. |
| locus_group              | A group name for a set of related locus types as defined by the HGNC (e.g. non-coding RNA).         |
| locus_type               | The locus type as defined by the HGNC (e.g. RNA, transfer).                                          |
| status                   | Status of the symbol report, which can be either "Approved" or "Entry Withdrawn".                    |
| location                 | Cytogenetic location of the gene (e.g. 2q34).                                                        |
| location_sortable        | Same as "location" but single digit chromosomes are prefixed with a 0 enabling them to be sorted.   |
| alias_symbol             | Other symbols used to refer to this gene as seen in the "SYNONYMS" field in the symbol report.       |
| alias_name               | Other names used to refer to this gene as seen in the "SYNONYMS" field in the gene symbol report.    |
| prev_symbol              | Symbols previously approved by the HGNC for this gene. Equates to the "PREVIOUS SYMBOLS & NAMES" field within the gene symbol report. |
| prev_name                | Gene names previously approved by the HGNC for this gene. Equates to the "PREVIOUS SYMBOLS & NAMES" field within the gene symbol report. |
| gene_family              | Name given to a gene family or group the gene has been assigned to. Equates to the "GENE FAMILY" field within the gene symbol report. |
| gene_family_id           | ID used to designate a gene family or group the gene has been assigned to.                          |
| date_approved_reserved   | The date the entry was first approved.                                                              |
| date_symbol_changed      | The date the gene symbol was last changed.                                                          |
| date_name_changed        | The date the gene name was last changed.                                                            |
| date_modified            | Date the entry was last modified.                                                                   |
| entrez_id                | Entrez gene ID. Found within the "GENE RESOURCES" section of the gene symbol report.                |
| ensembl_gene_id          | Ensembl gene ID. Found within the "GENE RESOURCES" section of the gene symbol report.                |
| vega_id                  | Vega gene ID. Found within the "GENE RESOURCES" section of the gene symbol report.                   |
| ucsc_id                  | UCSC gene ID. Found within the "GENE RESOURCES" section of the gene symbol report.                   |
| ena                      | International Nucleotide Sequence Database Collaboration (GenBank, ENA and DDBJ) accession number(s). Found within the "NUCLEOTIDE SEQUENCES" section of the gene symbol report. |
| refseq_accession         | RefSeq nucleotide accession(s). Found within the "NUCLEOTIDE SEQUENCES" section of the gene symbol report. |
| ccds_id                  | Consensus CDS ID. Found within the "NUCLEOTIDE SEQUENCES" section of the gene symbol report.        |
| uniprot_ids              | UniProt protein accession. Found within the "PROTEIN RESOURCES" section of the gene symbol report. |
| pubmed_id                | Pubmed and Europe Pubmed Central PMID(s).                                                            |
| mgd_id                   | Mouse genome informatics database ID. Found within the "HOMOLOGS" section of the gene symbol report. |
| rgd_id                   | Rat genome database gene ID. Found within the "HOMOLOGS" section of the gene symbol report.        |
| lsdb                     | The name of the Locus Specific Mutation Database and URL for the gene separated by a | character.    |
| cosmic                   | Symbol used within the Catalogue of somatic mutations in cancer for the gene.                        |
| omim_id                  | Online Mendelian Inheritance in Man (OMIM) ID.                                                       |
| mirbase                  | miRBase ID.                                                                                         |
| homeodb                  | Homeobox Database ID.                                                                               |
| snornabase               | snoRNABase ID.                                                                                      |
| bioparadigms_slc         | Symbol used to link to the SLC tables database at bioparadigms.org for the gene.                    |
| orphanet                 | Orphanet ID.                                                                                        |
| pseudogene.org           | Pseudogene.org.                                                                                     |
| horde_id                 | Symbol used within HORDE for the gene.                                                              |
| merops                   | ID used to link to the MEROPS peptidase database.                                                    |
| imgt                     | Symbol used within international ImMunoGeneTics information system.                                 |
| iuphar                   | The objectId used to link to the IUPHAR/BPS Guide to PHARMACOLOGY database.                         |
| kznf_gene_catalog        | ID used to link to the Human KZNF Gene Catalog.                                                      |
| mamit-trnadb             | ID to link to the Mamit-tRNA database.                                                              |
| cd                       | Symbol used within the Human Cell Differentiation Molecule database for the gene.                   |
| lncrnadb                 | lncRNA Database ID.                                                                                 |
| enzyme_id                | ENZYME EC accession number.                                                                         |
| intermediate_filament_db | ID used to link to the Human Intermediate Filament Database.                                         |
| agr                      | The HGNC ID that the Alliance of Genome Resources (AGR) have linked to their record of the gene. Use the HGNC ID to link to the AGR. |
| mane_select              | NCBI and Ensembl transcript IDs/acessions including the version number for one high-quality representative transcript per protein-coding gene that is well-supported by experimental data and represents the biology of the gene. The IDs are delimited by |. |


The data does not need to be to be downloaded separately, as it is pulled and parsed using the `requests` and `json` libraries. 

Citation:
HGNC. (2022). HGNC Dataset [Data file]. Retrieved from https://www.genenames.org/download/archive/


## Instructions to build a new image from your Dockerfile
- Build a docker image from your Dockerfile: `docker build -t gene_api .`
- Run the docker redis server: `docker run --rm -u $(id -u):$(id -g) -p 6379:6379 -d -v $PWD/data:/data redis:7 --save 1 1`
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


