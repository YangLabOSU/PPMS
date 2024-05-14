import argparse
import pandas as pd
import matplotlib.pyplot as plt

def parse_ppms_data(filename):
    """"
    This function parses the PPMS .dat file into a nicely formatted pandas dataframe

    Args:
    - filename: the file path of the PPMS .dat file(s) 
    """
    with open(args.filename, 'r') as file:
        # Find the start of the data section
        for r, line in enumerate(file):
            if line.strip().startswith('[Data]'):
                header_length = r+1
    df=pd.read_csv(args.filename, skiprows=header_length)
    return df

def plot_ppms_data(filename, plot_title, x_data, y_data, x_label, y_label):
    """
    Plot the relevant PPMS data.

    Args:
    - filename (str): Path to the PPMS data file.
    - plot_title (str): Title of the plot.
    - x_data (str): Name of the column for the x-axis.
    - y_data (arr): List of strings of the column for the y-axis.
    - x_label (str): Label for the x-axis.
    - y_label (str): Label for the y-axis.
    """
    data = parse_ppms_data(args.filename)
    x_data = args.x_data
    y_data = args.y_data
    plt.figure()
    for i in len(y_data):
        plt.plot(data[x_data], data[y_data[i]], marker='o', linestyle='-')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(plot_title)
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot data from a PPMS data file.')
    parser.add_argument('-f', '--filename' ,type=str, action='store', help='Path to the PPMS data file')
    parser.add_argument('-p', '--plot_title', type=str, default='PPMS Data Plot', help='Title of the plot')
    parser.add_argument('-x_data', type=str, default='Temperature (K)', help='Name of the column for the x-axis')
    parser.add_argument('-ydata', nargs='+', default=[], help='List of strings for the ydata to plot from the dataframe')
    parser.add_argument('-x_label', type=str, default='Temperature (K)', help='Label for the x-axis')
    parser.add_argument('-y_label', type=str, default='Resistance (Ohms)', help='Label for the y-axis')
    args = parser.parse_args()
    
    file_path = args.filename
    print('Reading in PPMS data file '+ args.filename)
    data = parse_ppms_data(args.filename)
    print('Plotting the following columns: '+ args.xdata)
    plot_ppms_data(args.filename, args.plot_title, args.x_data, args.y_data, args.x_label, args.y_label)