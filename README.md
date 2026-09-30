# Urban Analytics Dashboard

A simple Python data visualization project that compares **City A vs City B** across four urban analytics dimensions:

- Population growth trend
- Cost of living
- Climate / temperature distribution
- Income vs happiness

The dashboard is generated as a 2×2 Matplotlib figure and saved as `urban_dashboard.png`.

## Preview

The program creates one dashboard containing four charts:

1. **Population Growth** — 10-year normalized population index
2. **Cost of Living** — monthly costs across housing, food, transport, utilities, and health
3. **Climate Distribution** — simulated daily temperature distributions
4. **Income vs Happiness** — simulated income and happiness observations

## Requirements

- Python 3.9 or newer
- NumPy
- Matplotlib

This project **does not require a virtual environment**.

## Installation — Without venv

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/urban-analytics-dashboard.git
cd urban-analytics-dashboard
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Install the required packages

Install them for your normal/system Python:

```bash
python3 -m pip install -r requirements.txt
```

If your system uses `python` instead of `python3`:

```bash
python -m pip install -r requirements.txt
```

> On some Linux/macOS systems, pip may refuse to install packages globally. If that happens, use your operating system's Python package manager or a user-level installation such as `python3 -m pip install --user -r requirements.txt`. A virtual environment is not required by this project.

## Run the Dashboard

```bash
python3 Multiplotdashboard.py
```

or:

```bash
python Multiplotdashboard.py
```

The program will:

1. Generate the sample datasets.
2. Create the four visualizations.
3. Save the dashboard as:

```text
urban_dashboard.png
```

4. Open the Matplotlib plot window.

## Project Structure

```text
urban-analytics-dashboard/
│
├── Multiplotdashboard.py
├── requirements.txt
├── README.md
└── urban_dashboard.png   # generated after running the program
```

## Data Note

The project currently uses **simulated/sample data** rather than real city datasets. The climate and income/happiness data are randomly generated with a fixed NumPy seed so the results are reproducible.

## Technologies Used

- Python
- NumPy
- Matplotlib
- Data Visualization
- Basic Statistical Simulation

## What You Can Learn From This Project

This project demonstrates:

- Creating reusable Python functions
- Generating NumPy arrays
- Working with random data
- Line charts
- Bar charts
- Histograms
- Scatter plots
- Matplotlib subplots
- Figure titles, labels, legends, and grids
- Saving charts as PNG files

## Customization

You can modify:

- City names
- Population values
- Cost-of-living values
- Temperature distributions
- Income and happiness data
- Chart titles and labels
- Figure size
- Output image resolution

For example, change:

```python
fig.savefig("urban_dashboard.png", dpi=150)
```

to:

```python
fig.savefig("urban_dashboard.png", dpi=300)
```

for a higher-resolution output image.

## License

This project is provided for educational and portfolio use. You may modify and extend it for your own projects.
And planning to use real Dataset in Future for comparing real cities
