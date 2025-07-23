import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
df = pd.read_csv("C:\\Users\\Santhosh\\Documents\\ShadowFox\\Intermediate_tasks\\delhiaqi.csv")  # Replace with actual file path

# Step 2: Clean column names (remove leading/trailing spaces and unify case)
df.columns = df.columns.str.strip().str.upper()

# Step 3: Define pollutant columns (in uppercase to match cleaned columns)
pollutants = ['PM2.5', 'PM10', 'NO2', 'SO2', 'CO', 'NO', 'NH3']
pollutants = [p.upper() for p in pollutants]

# Step 4: Identify which pollutants are available in the dataset
available_pollutants = [p for p in pollutants if p in df.columns]

# Step 5: Display descriptive statistics for available pollutants
if available_pollutants:
    print("Descriptive statistics for pollutants:")
    print(df[available_pollutants].describe())
else:
    print("None of the specified pollutant columns were found in the dataset.")

# Step 6: Plot average pollutant levels (bar chart)
if available_pollutants:
    avg_pollutants = df[available_pollutants].mean()
    plt.figure(figsize=(8, 5))
    sns.barplot(x=avg_pollutants.index, y=avg_pollutants.values, palette="viridis")
    plt.title("Average Levels of Air Pollutants")
    plt.ylabel("Average Concentration")
    plt.xlabel("Pollutants")
    plt.tight_layout()
    plt.show()

# Step 7: (Optional) Show missing value counts
print("\nMissing values in pollutant columns:")
print(df[available_pollutants].isnull().sum())
