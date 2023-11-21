# Riskmapper (Risk Heatmap Generator)

The Risk Heatmap Generator is a Python script that reads an Excel file containing risk data and generates a heatmap visualization based on the provided risks. The heatmap represents the risks on a 10x10 grid, with colors indicating the level of risk.

## Features

- Reads risk data from an Excel file
- Generates a heatmap visualization based on risk levels
- Allows customization of color gradient, labels, and scale
- Supports exporting the heatmap as PNG, JPEG, TIFF, or PDF

## Prerequisites

- Python 3.x
- pandas
- matplotlib
- openpyxl

## Installation

1. Clone the repository or download the script file (`risk-heatmap.py`).

2. Install the required dependencies using pip:

   ```shell
   pip install pandas matplotlib openpyxl

## Usage

1. Prepare an Excel file with the risk data. The file should have the following columns:
   - `Likelihood`: The likelihood of the risk occurrence (numeric value between 1 and 10)
   - `Impact`: The impact of the risk (numeric value between 1 and 10)

2. Run the script with the following command:

   ```shell
   python risk-heatmap.py path/to/excel-file.xlsx

3. Follow the prompts to select the desired file format (PNG, JPEG, TIFF, or PDF).
4. The script will generate a heatmap visualization based on the risk data and save it as an image file.
