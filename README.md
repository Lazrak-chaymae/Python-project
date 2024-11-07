# Efficient Data Stream Anomaly Detection

## Project Overview

This project simulates a real-time data stream and detects anomalies in the data using a sliding window approach. The data stream is generated with regular patterns, random noise, and occasional anomalies. The system identifies and flags anomalies based on statistical measures like mean and standard deviation, and visualizes the results in real-time.

### Key Features:
- **Data Stream Simulation**: Generates a synthetic data stream with periodic patterns, noise, and occasional anomalies.
- **Anomaly Detection**: Detects outliers in the data using a sliding window approach based on the mean and standard deviation.
- **Real-Time Visualization**: Displays the data stream with anomalies marked, providing a visual representation of the data and detected outliers.
- **Real-Time Console Output**: Prints the data stream with anomalies highlighted in the console for a more detailed analysis.

## Requirements

The following dependencies are required to run the project:

- Python 3.x
- matplotlib

# Files
- **anomaly-detection.py**: The main script containing the logic for simulating the data stream, detecting anomalies, and visualizing the results.
- **requirements.txt**: A list of required Python packages for the project.
- **README.md**: This project documentation.

# How to Run
1-Download the Folder.
2-Install the required dependencies:

```bash
pip install -r requirements.txt
```

3-Run the script to simulate the data stream and detect anomalies:

```bash
python stream_anomaly_detection.py
```
# Example Output

After running the script, you will see the data stream printed to the console with anomalies marked, and a plot showing the data with red markers indicating the anomalies.

```bash
0: 0.118 <-- Anomaly
1: 0.236
2: 0.345
...
```
# Sample Plot:
A graph will display the data stream, with anomalies highlighted in red.


