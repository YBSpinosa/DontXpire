import pandas as pd
import streamlit as st
import os

#Las claves del dataframe son: "Title", "Ingredients", "Instructions"

#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame

#https://docs.streamlit.io/develop/api-reference

st.title(":red[_DontXpire_]")

st.subheader("If improvising is not your **strong point**", divider = "blue")




df = pd.read_csv('recipes_dataset.csv')
print(df.columns)     
print()
print(df.size)     
print()
print(df.iloc[0]['Instructions']) 

ingredient = input("Introduzca el nombre del ingrediente 1")

filtro = df['Ingredients'].str.contains(ingredient, case=False)
print(df[filtro].head()[['Title','Ingredients']])

