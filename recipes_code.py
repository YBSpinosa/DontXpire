import pandas as pd

df = pd.read_csv('recipes_dataset.csv')
print(df.columns)              # Title, Ingredients, Instructions
print(df.iloc[0]['Instructions'])  # Primer paso completo

# Buscar recetas que contengan "garlic"
filtro = df['Ingredients'].str.contains('garlic', case=False)
print(df[filtro].head()[['Title','Ingredients']])

