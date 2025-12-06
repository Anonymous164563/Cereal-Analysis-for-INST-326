
import pandas as pd  

#data take from https://www.kaggle.com/datasets/crawford/80-cereals 

print("\nReads the cereal csv file, data take from https://www.kaggle.com/datasets/crawford/80-cereals")
cereals = pd.read_csv("data/cereal.csv")   

cereals_Frame = pd.DataFrame(cereals)

print("\nFirst five rows read") 
print(cereals_Frame.head()) 

print("\nCereals Information") 
print(cereals_Frame.info()) 

print("\nSummary of statistics")
print(cereals_Frame.describe())  


print("\n Locating by column name using .loc(), ratings column located") 
print(cereals_Frame.loc[:,"rating"].head()) 

print(cereals_Frame.loc[cereals_Frame.index[0], "rating"])

print("\nLocating the single cell using .loc") 
print(cereals_Frame.loc[cereals_Frame.index[0]:cereals_Frame.index[4]])

print("\nFinding rows by position using iloc, first 5 rows extracted") 

print(cereals_Frame.iloc[0:5])

print("\nFinding column by position")
print(cereals_Frame.iloc[0, 2:5])

print("\nFiltering cereals whose calories are greather than 100") 
high_cal = cereals_Frame[cereals_Frame["calories"] > 100] 
print(high_cal.head()) 

print("\nFiltering cereals whose calroies are > 100 but sugar is < 10")  
comb_Filter = cereals_Frame[
    (cereals_Frame["calories"] > 100) & (cereals_Frame["sugars"] < 10)
]
print(comb_Filter.head())
print(comb_Filter.head())

print("\nCreating a new column called doubling the calories(caloriesX2)") 
cereals_Frame["caloriesX2"] = cereals_Frame["calories"] * 2 
print(cereals_Frame[["calories","caloriesX2"]].head()) 

print("\nDropping the caloriesX2 column") 

cereals_Frame = cereals_Frame.drop("caloriesX2", axis = 1) 
print("Columns still available", cereals_Frame.columns.tolist())  

print("\nGetting the rating based on average rating grouped by the cereal manufacture (mfr)") 

grouped = cereals_Frame.groupby("mfr")["rating"].mean() 
print(grouped)

    
