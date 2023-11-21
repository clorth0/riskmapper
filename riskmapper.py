import argparse
import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from datetime import datetime
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Generate a risk heatmap from an Excel file.',
                                 epilog='Ensure your Excel file has "Likelihood" and "Impact" columns.')
parser.add_argument('file', metavar='file', type=str, help='the location of the Excel file')
args = parser.parse_args()

# Get the file location from the parsed arguments
file_location = args.file

# Load the Excel file
try:
    df = pd.read_excel(file_location)
except FileNotFoundError:
    print('Could not find the file at the provided location. Please check the file path and try again.')
    sys.exit()  # Exit the script
except Exception as e:
    print(f'An error occurred while trying to read the file: {e}')
    sys.exit()  # Exit the script

# Check if 'Likelihood' and 'Impact' columns exist in the DataFrame
required_columns = ['Likelihood', 'Impact']
for column in required_columns:
    if column not in df.columns:
        print(f'Column "{column}" not found in the Excel file. Please ensure the Excel file contains the necessary columns.')
        sys.exit()  # Exit the script

# Multiply the 'Likelihood' and 'Impact' columns to get a 'Risk' column
df['Risk'] = df['Likelihood'] * df['Impact']

# Create a scatter plot using matplotlib
fig, ax = plt.subplots(figsize=(10, 10))

# Generate a color map ranging from white to red
cmap = mcolors.LinearSegmentedColormap.from_list("n",['#ffffff','#ff0000'])

# Create a color normalizer that will map the Risk values to the range 0-1
norm = plt.Normalize(df['Risk'].min(), df['Risk'].max())

sc = ax.scatter(df['Likelihood'], df['Impact'], c=df['Risk'], cmap=cmap, norm=norm)

# Set the limits of the plot to the range 1-10
ax.set_xlim(1, 10)
ax.set_ylim(1, 10)

# Create a colorbar
cbar = plt.colorbar(sc, ax=ax)

# The colorbar values range from the minimum to maximum risk values in the DataFrame
cbar_min = df['Risk'].min()
cbar_max = df['Risk'].max()

# Set the colorbar ticks and tick labels to represent the range of risk values
cbar_ticks = [cbar_min, cbar_max]  # Create ticks with the min and max risk values
cbar_tick_labels = [1, 100]  # Create tick labels for the range 1-100
cbar.set_ticks(cbar_ticks)  # Set the ticks of the colorbar
cbar.set_ticklabels(cbar_tick_labels)  # Set the tick labels

# Add the average and median Risk to the colorbar
avg_risk = df['Risk'].mean()
median_risk = df['Risk'].median()
cbar.ax.plot([0, 1], [avg_risk, avg_risk], color='blue', label='Average Risk')
cbar.ax.plot([0, 1], [median_risk, median_risk], color='green', label='Median Risk')

# Define the path to the icon image
icon_path = 'path/to/icon.png'

# Label each point in the scatter plot with an icon
for i, row in df.iterrows():
    icon = OffsetImage(plt.imread(icon_path), zoom=0.05)
    ab = AnnotationBbox(icon, (row['Likelihood'], row['Impact']), frameon=False)
    ax.add_artist(ab)

# Prompt for the desired file format
file_format = None
while file_format not in ('1', '2', '3', '4'):
    print('Select the file format:')
    print('1. PNG')
    print('2. JPEG')
    print('3. TIFF')
    print('4. PDF')
    file_format = input('Enter the number corresponding to the file format: ')

# Map the selected number to the corresponding file extension
file_extensions = {
    '1': 'png',
    '2': 'jpeg',
    '3': 'tiff',
    '4': 'pdf'
}

selected_format = file_extensions[file_format]

# Add the title to the plot
plt.title('Cybersecurity Health Check Scorecard', fontsize=16, fontweight='bold')

# Get the timestamp
timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Specify the desired file name based on the timestamp
file_name = f'heatmap_{timestamp}.{selected_format}'

# Save the plot as the selected file format
fig.savefig(file_name)
