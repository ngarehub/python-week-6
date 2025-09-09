# 1. Line Chart (just for demonstration, use petal length across dataset index)
plt.figure(figsize=(8,5))
plt.plot(df.index, df['petal length (cm)'], label="Petal Length")
plt.title("Line Chart: Petal Length Across Samples")
plt.xlabel("Sample Index")
plt.ylabel("Petal Length (cm)")
plt.legend()
plt.show()

# 2. Bar Chart: average petal length per species
plt.figure(figsize=(8,5))
grouped.plot(kind='bar', color=['red','green','blue'])
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram: distribution of sepal length
plt.figure(figsize=(8,5))
plt.hist(df['sepal length (cm)'], bins=20, color='skyblue', edgecolor='black')
plt.title("Histogram: Sepal Length Distribution")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot: Sepal length vs Petal length
plt.figure(figsize=(8,5))
sns.scatterplot(data=df, x="sepal length (cm)", y="petal length (cm)", hue="species")
plt.title("Scatter Plot: Sepal Length vs Petal Length by Species")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.show()
