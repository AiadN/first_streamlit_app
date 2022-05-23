import streamlit
streamlit.title('My parents new healthy diner')
streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruit:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

Fruit_selected = streamlit.multiselect("Pick some fruit:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
Fruit_to_show = my_fruit_list.loc[Fruit_selected]

streamlit.dataframe(Fruit_to_show)
