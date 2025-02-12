# Reduced Bacterial Growth Assays 

This assay aims to quantify the infectivity of bacteriophages using bacterial growth curves. We are currently using two versions of this project. 
- **Version 0**: Defines the range of starting densities at which there is no significant correlation between starting and ending densities of bacterial growth, and quantifies optimal phage concentration
- **Version 1**: Checks for internal variability within biological + technical replicates, both with and without phage.
- **Version 2**: Optimizes the starting concentration of phage and quantifies the timepoint of maximum virulence. <br><br>

# Navigation

[Go to Version 0](#version-0) <br>
[Go to Version 1](#version-1)  
[Go to Version 2](#version-2)  <br>
[Files](#files)

# Version 0

### Procedure
<br><br>
# Version 1

## Day 1

### Procedure
1. Pipette 90 uL KB broth into 96 well plate
2. Grab freezer stock of DC3000, and scrape about 20 uL into an empty well
3. Pipette 10 uL of DC into broth, dilute to appropriate concentration
4. Plate <br><br>

## Day 2

### Procedure
1. Pick 8 colonies into a 24 well containing ~2 mL of KB broth <br><br>

## Day 3

### Procedure
1. Split the 96-well plate into halves: one with phage, one without.
2. Pipette each row of biological replicates into a media reservoir.
3. Transfer liquid from reservoir to a 96-well plate.
4. Back dilute to a starting density of 0.2-0.3.
5. Pipette ~180 µL bacteria and ~10 µL phage <br><br>

[Back to Top](#reduced-bacterial-growth-assays) <br><br>

# Version 2 

## [Day 1](#day-1)

## Day 2

### Procedure
1. Pick 4 colonies into a 24 well containing ~2 mL of KB broth <br><br>

## Day 3
honestly maybe just insert a picture of the set up that would be easier <br><br>

[Back to Top](#reduced-bacterial-growth-assays)


# Files

### tools.py

Simple Functions for data visualization

**clean_and_transpose(df, start_row=32, end_row=106)**

**phage_conc_sep(df)**
- separates wells 1-6 from wells 7-12
- returns two dataframes

**plot_timeseries(dataframe, title = None)**
- add optional graph title
- plots one time series per column in dataframe
  
**remove_outliers(df, fifteen_min = 1, lower_bound = 0.15, upper_bound = 0.25)**
- keeps only the columns in which the row specified meets the specific lower and upper bounds stated in fxn
- fifteen_min: specify the row that will be filtered

**AUC_graph(df, title = None)**
- AUC values calculated for every column in the dataframe
-  KDE plot (histogram + probability density curve) for each column

**rsquared(x, y)**

**plot_with_r_squared(df, x_col, y_col, lower = 0, upper=20, decimals=4, title = None)**



