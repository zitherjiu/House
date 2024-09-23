import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

st.title('California Housing Data(1990) by Xinyue Zhou :')
df = pd.read_csv('Housing.csv')
housing_data = st.slider('Minimal Median House Price', 0, 500001, 200000)  # min, max, default

# create a multi select
location_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults
# create a radio button
income_level = st.sidebar.radio(
    "Choose income level:",
    ('Low','Median','High')
    )

st.subheader('See more filters in the sidebar:')

# filter based on selected income level
if income_level == 'Low':
    filtered_df = df[df['median_income'] <= 2.5]
elif income_level == 'Median':
    filtered_df = df[(df['median_income'] > 2.5) & (df['median_income'] < 4.5)]
else:
    filtered_df = df[df['median_income'] >= 4.5]

# filter by Minimal Median House Price
filtered_df = filtered_df[filtered_df['median_house_value'] > housing_data]

# filter by location type
filtered_df = filtered_df[filtered_df['ocean_proximity'].isin(location_filter)]

st.map(filtered_df)

# show the plot
st.subheader('Median House Value')
fig, ax = plt.subplots(figsize=(10, 5))
filtered_df['median_house_value'].hist(bins=30,ax=ax)

st.pyplot(fig)
