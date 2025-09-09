print("\nBasic Statistics:")
print(df.describe())

# Grouping: average petal length per species
grouped = df.groupby('species')['petal length (cm)'].mean()
print("\nAverage Petal Length per Species:")
print(grouped)
