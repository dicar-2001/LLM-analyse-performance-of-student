import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

data = pd.read_csv("C:/Users/FHM/Downloads/SMP-SMC-SMA-SMI-S2-17-18.csv")

# Extract columns starting from index 4
print(data.columns.tolist())

# Step 1: Convert columns to numeric, forcing non-numeric values to NaN
data2 = pd.DataFrame({
   'Electricité': pd.to_numeric(data['Electricité'], errors='coerce'),
   'Analyse.2': pd.to_numeric(data['Analyse.2'], errors='coerce'),
   'Algèbre.2': pd.to_numeric(data['Algèbre.2'], errors='coerce'),
   'Math': pd.to_numeric(data['Math'], errors='coerce'),
   'LT': pd.to_numeric(data['LT'], errors='coerce'),
   'Note.du.Semestre2': pd.to_numeric(data['Note.du.Semestre2'], errors='coerce')
})

# Step 2: Drop rows with missing values (if you want to remove incomplete rows)

# Step 3: Alternatively, you can fill missing values with the column mean (if you don't want to drop data)
data_filled = data2.fillna(data2.mean())

# Print the cleaned data
print(data_filled.head())  # Or print(data_filled.head())

pca = PCA(n_components=2)
principal_components = pca.fit_transform(data_filled )

pca_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])

plt.figure(figsize=(8,6))
plt.scatter(pca_df['PC1'], pca_df['PC2'])
plt.title('PCA of Student Performance')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()