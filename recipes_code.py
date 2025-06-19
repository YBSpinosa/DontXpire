import pandas as pd
import streamlit as st
import os


#Las claves del dataframe son: "Title", "Ingredients", "Instructions"

#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html#pandas.DataFrame

#https://docs.streamlit.io/develop/api-reference

if "actual_page" not in st.session_state:
    st.session_state.actual_page = "Home"

if st.session_state.actual_page == "Home":
    st.title(":red[_DontXpire_] 🍝", width = 300)
    st.subheader("If improvising is not your ***STRONG*** point", divider = "green", width = 500)

    description = "DontXpire has access to a dataset with over ***13000*** recipes to provide you" \
    " with some of the most delicious and unique dishes you could think of." \
    "\n\nTell us the ingredients to work with and let our algorithm do the rest!"
    st.markdown(description)
    st.divider()

    #Hay que pasar un multiselect con todos los ingredientes en una lista, pensar en como obtenerlos

    ingredients = ["garlic", "milk", "chicken breasts", "chickpeas", "peas", "tomato", "potato"]
    ingredients_selection = st.multiselect("Write down up to ***15*** ingredients. When you are done, press :blue-background[continue]",
                                max_selections=15,
                                options= ingredients)
    valid_input = True
    if not ingredients_selection:
        st.warning("You must select at least one ingredient!", icon = "⚠️")
        valid_input = False
    
    col1, col2, col3 = st.columns([4, 2, 4])
    if valid_input:
        with col2:
            toPage2 = st.button(":blue-background[continue]", type = "secondary", use_container_width= True)
        if toPage2:
            st.session_state.actual_page = "Page2"
            st.rerun()
else:
    col1, col2 = st.columns([5, 2])
    with col1:
        st.title(":red[_DontXpire_] 🍝", width = 300)
    with col2:
        toHome = st.button("***BACK***", type = "secondary")
    
    if toHome:
        st.session_state.actual_page = "Home"
        st.rerun()



#df = pd.read_csv('recipes_dataset.csv')
#print(df.columns)     
#print()
#print(df.size)     
#print()
#print(df.iloc[0]['Instructions']) 






