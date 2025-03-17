# Reduced Bacterial Growth Assays 

This assay aims to quantify the infectivity of bacteriophages using bacterial growth curves. We are currently using two versions of this project. 
- **Version 0**: Defines the range of starting densities at which there is no significant correlation between starting and ending densities of bacterial growth, and quantifies optimal phage concentration
- **Version 1**: Checks for internal variability within biological + technical replicates, both with and without phage.
- **Version 2**: Measure OD of standard concentration of host challenged with a large range of phage concentrations, capture response to relevant biological variation in phage concentration (by testing different orders of magnitudes)
-  two things: average measure of host resistance, variation within a population of host resistance figured out by MIC like graph <br><br> 

# Navigation

[Go to Version 0](#version-0) <br>
[Go to Version 1](#version-1)  
[Go to Version 2](#version-2)  <br>
[Files](#files)

# Version 0

## Day 1

### Procedure
1. Pour broth into media reservoir
2. Pipette 90 uL KB broth into 96 well plate
3. Hustle responsibly to and from freezer, grab DC stock
4. Put around 20 uL into well plate, away from the dil series
5. Perform 10 fold serial dilution (10 uL into each)
6. Plate 90 uL with beads <br><br>
 ## Day 2

 ### Procedure
 1. In a 96 well, pipette 100 uL KB
 2. Pick 96 colonies <br><br>
 
 ## Day 3

 ### Procedure
 1. 900 uL phage buffer into 24 well plate (flat bottom)
 2. 10 fold dilution of phage to working concentration concentration (100 uL into each)
 3. Back dilute to around 0.2
 4. Split plate in half, 10 uL of 1000 PFU and other half 10000 PFU phage into each well <br><br>


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
1. Split 96 well into 4 sections for 4 biological replicates
2. Read OD on plate reader
3. Pipette each biological replicate into a media reservoir
4. Dilute to a range between 0.15-0.25
5. Create a dilution series of phage from -1 to -6
6. Pipette 10 uL phage dilution series into each column of 96 well containing 180 uL bacteria
7.  <br><br>

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
- KDE plot (histogram + probability density curve) for each column
- Returns a normal test (p <= 0.05 -> curve is normal, p > 0.05 -> curve is not normal)

**rsquared(x, y)**
- returns the strength and direction of the linear relationship between x and y

**plot_with_r_squared(df, x_col, y_col, lower = 0, upper=20, decimals=4, title = None)**


[Back to Top](#reduced-bacterial-growth-assays)

