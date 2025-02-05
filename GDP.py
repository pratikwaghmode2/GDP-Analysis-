import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "GDPdataset.csv"
df = pd.read_csv(file_path)

# Drop unnecessary columns
df.drop(columns=["Indicator Name", "Indicator Code", "Country Code"], inplace=True)

# Melt the dataset to long format
df_melted = df.melt(id_vars=["Country Name"], var_name="Year", value_name="GDP")

# Convert Year to numeric and GDP to float
df_melted["Year"] = pd.to_numeric(df_melted["Year"], errors="coerce")
df_melted["GDP"] = pd.to_numeric(df_melted["GDP"], errors="coerce")

# Drop NaN values
df_melted.dropna(inplace=True)

# Get top 10 economies in 2023
df_2023 = df_melted[df_melted["Year"] == 2023].sort_values(by="GDP", ascending=False).head(10)

# Plot top 10 economies
plt.figure(figsize=(12, 6))
sns.barplot(x="GDP", y="Country Name", data=df_2023, palette="viridis")
plt.xlabel("GDP in Trillions (US$)")
plt.ylabel("Country")
plt.title("Top 10 Economies in 2023")
plt.xscale("log")
plt.show()
plt.savefig("Top 10 Economies")
# GDP Trend for Selected Countries
selected_countries = ["United States", "China", "India", "Germany", "United Kingdom"]
df_selected = df_melted[df_melted["Country Name"].isin(selected_countries)]

plt.figure(figsize=(12, 6))
sns.lineplot(data=df_selected, x="Year", y="GDP", hue="Country Name")
plt.xlabel("Year")
plt.ylabel("GDP (US$)")
plt.title("GDP Growth Trends (1960-2023)")
plt.legend(title="Country")
plt.show()
plt.savefig("GDP_TREND")
# Calculate GDP Growth Rate
df_melted.sort_values(by=["Country Name", "Year"], inplace=True)
df_melted["GDP Growth Rate"] = df_melted.groupby("Country Name")["GDP"].pct_change() * 100

# Plot GDP Growth Rate of Top 5 Economies in 2023
top_5_countries = df_2023["Country Name"].head(5)
df_growth = df_melted[df_melted["Country Name"].isin(top_5_countries)]

plt.figure(figsize=(12, 6))
sns.lineplot(data=df_growth, x="Year", y="GDP Growth Rate", hue="Country Name")
plt.xlabel("Year")
plt.ylabel("GDP Growth Rate (%)")
plt.title("GDP Growth Rate of Top 5 Economies")
plt.axhline(y=0, color='black', linestyle='--')
plt.legend(title="Country")
plt.show()
plt.savefig("GDP Growth rate")