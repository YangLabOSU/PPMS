import argparse
import pandas as pd
import matplotlib.pyplot as plt

def parse_ppms_data(file_path):
    """"
    This function parses the PPMS .dat file into a nicely formatted pandas dataframe

    Args:
    - file_path: the file path of the PPMS .dat file(s) 
    """
    with open(args.file_path, 'r') as file:
        # Find the start of the data section
        for r, line in enumerate(file):
            if line.strip().startswith('[Data]'):
                header_length = r+1
    df=pd.read_csv(args.file_path, skiprows=header_length)
    return df

def plot_ppms_data(file_path, plot_title, x_data, y_data, x_label, y_label):
    """
    Plot the PPMS data.

    Args:
    - file_path (str): Path to the PPMS data file.
    - plot_title (str): Title of the plot.
    - x_data (str): Name of the column for the x-axis.
    - y_data (str): Name of the column for the y-axis.
    - x_label (str): Label for the x-axis.
    - y_label (str): Label for the y-axis.
    """
    data = parse_ppms_data(file_path)
    plt.figure()
    plt.plot(data[x_data], data[y_data], marker='o', linestyle='-')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(plot_title)
    plt.grid(True)
    plt.show()


file_path = 'D979_Nb(100nm)_ch1_D980_Ge(5nm)_Nb(100nm)_ch3_RvsT.dat'
data = parse_ppms_data(file_path)
plot_ppms_data(args.file_path, args.plot_title, args.x_data, args.y_data, args.x_label, args.y_label)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Plot data from a PPMS data file.')
    parser.add_argument('--f', type=str, help='Path to the PPMS data file')
    parser.add_argument('--plot_title', type=str, default='PPMS Data Plot', help='Title of the plot')
    parser.add_argument('--x_data', type=str, default='Temperature (K)', help='Name of the column for the x-axis')
    parser.add_argument('--y_data', type=str, default='Bridge 1 Resistance (Ohms)', help='Name of the column for the y-axis')
    parser.add_argument('--x_label', type=str, default='Temperature (K)', help='Label for the x-axis')
    parser.add_argument('--y_label', type=str, default='Bridge 1 Resistance (Ohms)', help='Label for the y-axis')
    args = parser.parse_args()
