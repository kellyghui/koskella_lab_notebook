# File Structure

```
├── General Protocols
    └── e.g. making rif, amplifying phage, etc.
├── RBG_2024_5
    ├── Readme (Procedures)
    ├── Version 0
        ├── 10/3/2024
        └── 10/31/2024
    ├── Version 1
    └── Version 2
        ├── 3/03/2025
        ├── 3/10/2025
        └── 3/14/2025
├── RBG_Senior_Thesis
    ├── Final Thesis Proposal
    ├── ..
    └── ..
├── Daily Lab Notes
└── Python Functions for Growth Curve Analysis
```

# Files

## tools.py

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

**plot_biol_rep(df, num_bio_rep=8, num_tech_reps=3)**
- According to plate setup from RBG_Senior_Thesis 
- num_bio_rep: number of biological replicates (each biological replicate is one row of the plate)
- num_tech_reps: number of technical replicates (default is 3 technical replicates per biol rep, with tech replicates being every 3 columns of 96 well)
- Returns one plot for each biological replicate containing one line for each phage concentration (technical reps averaged)

 **plot_dose_response(df, pfu, num_tech_reps=3)**
 - Creates dose-response curves (OD vs log(PFU)) for each hour 0–15, one line per biological replicate 
 - Input pfu ranges like so - [0, 1e3, 1e5, 1e7]
 - num_tech_reps: default is 3 technical replicates per biol rep, with tech replicates being every 3 columns of 96 well
