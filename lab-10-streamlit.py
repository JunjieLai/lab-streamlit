import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')


st.title('California Housing Data (1990) by Junjie Lai')
df = pd.read_csv('housing.csv')

# note that you have to use 0.0 and 40.0 given that the data type of population is float
value_filter = st.slider('Median House Value:', 0.0, 500000.0, 200000.6)  # min, max, default

# create a multi select
location_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults

# create a input form
genre = st.sidebar.radio(
    "Choose income level",
    ('Low', 'Medium', 'High'))


# filter by median income
df = df[df.median_house_value <= value_filter]

# filter by location
df = df[df.ocean_proximity.isin(location_filter)]

# filter by median income
if genre == 'Low':
    df = df[df.median_income <= 2.5]
elif genre == 'Medium':
    df = df[(df.median_income > 2.5) & (df.median_income < 4.5)]
else:
    df = df[df.median_income > 4.5]

# show on map
st.map(df)


# show the plot
st.subheader('Histogram of the Median House Value')
fig, ax = plt.subplots(figsize=(20, 15))
df.median_house_value.hist(bins=30)
st.pyplot(fig)