import pandas as pd
import streamlit as st

#Las claves del dataframe son: "Title", "Ingredients", "Instructions"

#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame

#https://docs.streamlit.io/develop/api-reference

df = pd.read_csv('recipes_dataset.csv')
print(df.columns)     
print()
print(df.size)     
print()
print(df.iloc[0]['Ingredients']) 

ingredient = input("Introduzca el nombre del ingrediente 1")

filtro = df['Ingredients'].str.contains(ingredient, case=False)
print(df[filtro].head()[['Title','Ingredients']])

