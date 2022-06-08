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

#lets put  apick list here so they can pick the fruit
Fruits_selected = streamlit.multiselect("Pick some fruit:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
Fruits_to_show = my_fruit_list.loc[Fruits_selected]

#display the table
streamlit.dataframe(Fruits_to_show)


#new section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')

import requests 
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ "kiwi")
#streamlit.text(fruityvice_response.json()) #just writes the data to the screen

#take the json version of the response
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output as a table
streamlit.dataframe(fruityvice_normalized)

