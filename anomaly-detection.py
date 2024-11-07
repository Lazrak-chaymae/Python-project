import math
import random
import time
import matplotlib.pyplot as plt
from collections import deque

# ==============================================================================
# Project Documentation
# ==============================================================================
# This project simulates a data stream and detects anomalies in real-time using 
# a sliding window approach. The script generates a data stream with regular 
# patterns, noise, and occasional anomalies. Anomalies are detected based on 
# statistical measures (mean and standard deviation) within a sliding window.
# ==============================================================================

def generate_data_stream(size=100, period=20, noise=0.5, anomaly_chance=0.1):
    """
    Generates a data stream with seasonal patterns, noise, and occasional anomalies.

    Args:
        size (int): The number of data points to generate (default is 100).
        period (int): The period of the seasonal pattern (default is 20).
        noise (float): The amount of random noise to add to the data (default is 0.5).
        anomaly_chance (float): The probability of introducing an anomaly at each point (default is 0.1).

    Returns:
        List[float]: A list of generated data points, including seasonal patterns, noise, and anomalies.
    """
    data = []
    for i in range(size):
        base = math.sin(2 * math.pi * i / period)  # seasonal pattern
        random_noise = random.uniform(-noise, noise)  # adding some random noise
        value = base + random_noise
        if random.random() < anomaly_chance:  # randomly adding some anomalies
            value += random.uniform(5, 10)
        data.append(value)
    return data

def mean(data):
    """
    Computes the mean of a list of numbers.

    Args:
        data (List[float]): The list of numbers to calculate the mean for.

    Returns:
        float: The mean value of the list.
    """
    return sum(data) / len(data)

def std_dev(data, mean):
    """
    Computes the standard deviation of a list of numbers.

    Args:
        data (List[float]): The list of numbers to calculate the standard deviation for.
        mean (float): The mean value of the list.

    Returns:
        float: The standard deviation of the list.
    """
    return math.sqrt(sum((x - mean) ** 2 for x in data) / len(data))

def detect_anomalies(data, window_size=20, threshold=3):
    """
    Detects anomalies in a data stream using a sliding window approach and z-score threshold.

    Args:
        data (List[float]): The data stream to analyze.
        window_size (int): The size of the sliding window (default is 20).
        threshold (float): The z-score threshold for anomaly detection (default is 3).

    Returns:
        List[Tuple[int, float]]: A list of tuples where each tuple contains the index and value of an anomaly.
    """
    anomalies = []
    window = deque(maxlen=window_size)  # Efficient deque for sliding window
    mean_val = 0
    std_val = 0

    for i, value in enumerate(data):
        window.append(value)

        if len(window) == window_size:
            # Calculate mean and std for the current window
            if i == window_size - 1:
                mean_val = mean(window)
                std_val = std_dev(window, mean_val)
            
            # Anomaly detection based on z-score
            if abs(value - mean_val) > threshold * std_val:
                anomalies.append((i, value))
    return anomalies

def plot_stream(data, anomalies):
    """
    Plots the data stream and highlights anomalies on a graph.

    Args:
        data (List[float]): The data stream to plot.
        anomalies (List[Tuple[int, float]]): A list of anomalies to highlight on the plot.
    
    Displays:
        A plot showing the data stream with anomalies marked in red.
    """
    indices = list(range(len(data)))
    anomaly_indices = [i for i, _ in anomalies]
    anomaly_values = [value for _, value in anomalies]
    
    plt.plot(indices, data, label='Data Stream', color='black')
    plt.scatter(anomaly_indices, anomaly_values, color='red', label='Anomalies')
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('Data Stream with Anomalies')
    plt.legend()
    plt.show()

def print_stream(data, anomalies):
    """
    Prints the data stream and highlights anomalies in the console.

    Args:
        data (List[float]): The data stream to display.
        anomalies (List[Tuple[int, float]]): A list of anomalies detected in the stream.
    
    Prints:
        Each data point with an indication of whether it is an anomaly.
    """
    anomaly_indices = set(index for index, _ in anomalies)  # Store anomaly indices in a set for O(1) lookup
    for i, value in enumerate(data):
        if i in anomaly_indices:
            print(f"{i}: {value} <-- Anomaly")
        else:
            print(f"{i}: {value}")
        time.sleep(0.05)

if __name__ == "__main__":
    try:
        # Generate sample data stream
        stream = generate_data_stream()

        # Detect anomalies
        found_anomalies = detect_anomalies(stream)

        # Display the stream and detected anomalies
        print_stream(stream, found_anomalies)

        # Plot the data and anomalies
        plot_stream(stream, found_anomalies)

    except Exception as e:
        print(f"An error occurred: {e}")
