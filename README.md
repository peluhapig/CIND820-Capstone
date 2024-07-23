**Read Me File For Final Results**

All python files included are commented.

The CSV Files included in the repo are:
- zip_codes.csv : used for active NYS Zip Codes
- mi.csv : census data by Zip code used for Median Income
- sample_cars.csv : not used, generated for previous version but useful for viewer to get an idea of the data we used as the main dataset was too big to include
- sample_zips.csv : Number of cars of each make registered by zip code
- data_classes.csv : The same as above with an added column of classified income, 0 being lowest, 4 being highest
- norm_data_classes.csv: The same as above but normalized

The Python files included are:
- number_of_makes_per_zip.py : this generates the sample_zips file, it counts the total number of cars of certain makes in each zip code.
- data_census_combination.py : this generates the data_classes file and adds classes corresponding to median income to each Zip.
- zip_prediciton.py: This contains all of the predictive models of our project. I attempted to comment it very thoroughly.
- normalization.py: this normalizes our data_classes and outputs norm_data_classes. I got worse results when using it to predict but it may prove useful in the future or for visualization.



Data sources:

- NYS Registration Data: https://data.ny.gov/Transportation/Vehicle-Snowmobile-and-Boat-Registrations/w4pv-hbkt/about_data

- Census Data: https://data.census.gov/table?q=S1903:%20Median%20Income%20in%20the%20Past%2012%20Months%20(in%202022%20Inflation-Adjusted%20Dollars)&g=040XX00US36$8600000
