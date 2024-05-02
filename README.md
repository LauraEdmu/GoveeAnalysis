# Govee Temperature and Humidity Data Analysis

## Overview
This Python script is designed to analyze temperature and humidity data collected from a Govee smart thermometer. The script calculates various statistics including maximum, minimum, mean, median, mode, standard deviation, and skewness for both temperature and humidity data.

## Prerequisites
- Python 3.x
- pandas library
- numpy library
- scipy library

## Installation
To install the required libraries, run the following command in your terminal:

```bash
pip install pandas numpy scipy
```

## Usage
1. Place your `.csv` data file in the same directory as the script, or modify the `file_path` in the `main()` function to point to the location of your data file.
2. Run the script using Python:

```bash
GoveeAnalysis.py
```

The script will print the calculated statistics for both temperature and humidity directly to the console.

## Output
The output will display the following statistics for both temperature and relative humidity:
- Max
- Min
- Difference (Max - Min)
- Mean
- Median
- Mode (calculated based on the specified block size)
- Standard Deviation
- Skewness

## License
This project is licensed under the GNU GPL V3.0 License - see the LICENSE file for details.