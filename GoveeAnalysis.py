import pandas as pd
import numpy as np
from scipy import stats

def calculate_statistics(series, block_size):
    # Calculating various statistics for the given data series
    stats_data = {
        'max': series.max(),
        'min': series.min(),
        'diff': series.max() - series.min(),
        'mean': series.mean(),
        'median': np.median(series),
        'mode': stats.mode(np.round(series / block_size) * block_size, keepdims=True)[0][0],
        'std_dev': series.std(),
        'skewness': series.skew()
    }
    stats_data = {
        'max': f"{stats_data['max']:.1f}",
        'min': f"{stats_data['min']:.1f}",
        'diff': f"{stats_data['diff']:.1f}",
        'mean': f"{stats_data['mean']:.1f}",
        'median': f"{stats_data['median']:.1f}",
        'mode': f"{stats_data['mode']:.1f}",
        'std_dev': f"{stats_data['std_dev']:.1f}",
        'skewness': f"{stats_data['skewness']:.1f}"
    }
    return stats_data

def main():
    # Path to the CSV file
    file_path = 'data.csv'  # Modify this to the path of your CSV file
    
    # Load the data
    data = pd.read_csv(file_path)

    block_size_temp = 1  # The blocksize to group dat in, for use when calculating mode
    block_size_rh = 1    # Same as above for rh

    # Calculating statistics for temperature and relative humidity
    temp_stats = calculate_statistics(data[' Temperature_Celsius'], block_size_temp)
    rh_stats = calculate_statistics(data['Relative_Humidity'], block_size_rh)

    # Output the results
    print("Temperature Statistics: (deg)")
    for key, value in temp_stats.items():
        print(f"{key.capitalize()}: {value}")

    print("\nRelative Humidity Statistics: (RH%)")
    for key, value in rh_stats.items():
        print(f"{key.capitalize()}: {value}")

if __name__ == '__main__':
    main()
