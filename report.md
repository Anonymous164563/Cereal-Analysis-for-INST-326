Data Anaysis Report - Cereal File

For this dataset, I analyzed the 80 Cereals dataset from Kaggle. Containing infomration regarding 77 breakfast cereals. The attrbutes for the cereals included, calories, protein, fat, suga, sodium, fiber weight, cups per serving and overall rating. The dataset contained categorical variables like manufacturer("mfr") and if the ceral is hot and cold("type") 

Operations Performed 

- First thing I did was load the data into a pandas DatFrame which enabled me to read the csv file in Python and it's contents. Examining the DatFrame using .head(), .info(),.describe() respectively to understand the overall strucutre of the dataframe, including, its numerical statistics. Accessing data using .loc() and iloc() enabled retrieving single values, extracting row information and specific columns. 

- Two Boolean filters were created. One for selecting cereals with more than 100 calories, the other for selecting with 100 calories and sugars less than 10 grams. 

- Created a new column called "caloriesX2" which demosntrated potential to add columns, removing them using the .drop() method.

- Groupby method was used to calculate the average cereal rating grouped by each manufacturer

Observations 

- Overall the data set was clean and neat, making it easy to extract the information. No missing values in the columns.

- The average calories per serving was around 107

- Ratings varied widely

- Some cereals scored higher, while some received low ratings

- The manufactureres varied regarding their ratings. Some brands socred higher than others

- Higher calorie cereals contained more sugar, boolean filtering showed several exceptions

Limitations and Odd Findings 

- Some columns had categorical codes reuqiring a lookup table to fully understand(MFR)> Some cereals had overly high ratings compared to other brands, indicating societal bias towards brand name and recognition

- Despite a clean dataset, the cereal selection is only representative of the time of creation, not reflective in current market trends.
  
