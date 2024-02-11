# Analyzing NASA's Meteorite Landings Dataset

## Project Objective
This project aims to provide functions to analyze data from NASA's meteorite landings dataset. By processing and analyzing this data, researchers and enthusiasts can gain insights into the distribution and characteristics of meteorite landings, contributing to our understanding of celestial events and planetary science.

## Folder Contents
- `gcd_algorithm.py`: Contains the function for calculating the great circle distance algorithm.
- `ml_data_analysis.py`: Contains functions for data analysis and processing, including `summary_stats`, `remove_nulls`, and `calculate_distance`.

## Python Script Descriptions
- `gcd_algorithm.py`: Includes a function for calculating the great circle distance algorithm.
- `ml_data_analysis.py`: Utilizes the function from `gcd_algorithm.py` to compute distances based on specified parameters from the dataset. It includes the following functions:
  - `summary_stats()`: Prints the mean and median of the dataset for a given list of dictionaries and key strings.
  - `remove_nulls()`: Removes null values from a datasheet.
  - `calculate_distance()`: Computes the distance using the function from `gcd_algorithm.py`.

## Obtaining Data
- The dataset is sourced from NASA's meteorite landings dataset. It needs to be downloaded from NASA's website and copied to your personal computer.

## Running the Code
1. Ensure Python 3 is installed on your system.
2. Download the `gcd_algorithm.py` and `ml_data_analysis.py` scripts.
3. Download the meteorite landings dataset from NASA's website.
4. Place the dataset in the same directory as the Python scripts.
5. Open a terminal or command prompt and navigate to the directory containing the scripts and dataset.
6. Run the script `ml_data_analysis.py` using the Python interpreter: `python3 ml_data_analysis.py`.
7. Interpret the results by observing the cleaned data, summary statistics, or computed distances printed in the terminal.
