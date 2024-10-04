import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('dashboard\main_data.csv')

# Title of the dashboard
st.title('E-Commerce Customer Analysis')

# Introduction
st.write("""
In the ever-evolving world of e-commerce, understanding customer behavior and demographics is crucial for businesses aiming to thrive in a competitive market. This analysis focuses on customer distribution based on geographic locations, specifically cities and postal codes, using data from a leading e-commerce platform.

By examining this data, I aim to uncover insights into where customers are located and how these distributions can inform marketing strategies and business decisions. In the following sections, I will present the results of my analysis, highlighting key trends and implications for the business.
""")

# Problem Questions
st.subheader("Problem Questions")
st.write("""
1. What is the distribution of customers based on cities?
2. How does customer distribution vary according to postal codes?
""")

# Question 1: Distribution of customers by city
st.subheader('Distribution of Customers by City')
city_distribution = df['customer_city'].value_counts().reset_index()
city_distribution.columns = ['customer_city', 'customer_count']
top_cities = city_distribution.head(10)

# Plot 1: Bar plot for top 10 cities by customer count
fig1, ax1 = plt.subplots()
colors = ['lightblue' if city == top_cities.iloc[0, 0] else 'lightgray' for city in top_cities['customer_city']]
sns.barplot(x='customer_count', y='customer_city', data=top_cities, palette=colors, ax=ax1)
ax1.set_title('Top 10 Cities by Customer Count (Bar Plot)')
ax1.set_xlabel('Number of Customers')
ax1.set_ylabel('City')
st.pyplot(fig1)

# Plot 2: Pie chart for top 10 cities by customer count
fig2, ax2 = plt.subplots()
ax2.pie(top_cities['customer_count'], labels=top_cities['customer_city'], autopct='%1.1f%%', colors=['lightblue'] + ['lightgray'] * (len(top_cities) - 1), startangle=90)
ax2.set_title('Top 10 Cities by Customer Count (Pie Chart)')
ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig2)

# Question 2: Distribution of customers by postal code (Corrected)
st.subheader('Distribution of Customers by Postal Code')
postal_distribution = df['customer_zip_code_prefix'].value_counts().reset_index()
postal_distribution.columns = ['customer_zip_code_prefix', 'customer_count']
top_postal_codes = postal_distribution.head(10)

# Plot 3: Bar plot for top 10 postal codes by customer count (Corrected x and y axes)
fig3, ax3 = plt.subplots()
colors_postal = ['lightblue' if postal == top_postal_codes.iloc[0, 0] else 'lightgray' for postal in top_postal_codes['customer_zip_code_prefix']]
sns.barplot(x='customer_count', y='customer_zip_code_prefix', data=top_postal_codes, palette=colors_postal, ax=ax3)
ax3.set_title('Top 10 Postal Codes by Customer Count (Bar Plot)')
ax3.set_xlabel('Number of Customers')
ax3.set_ylabel('Postal Code')
st.pyplot(fig3)

# Plot 4: Pie chart for top 10 postal codes by customer count
fig4, ax4 = plt.subplots()
ax4.pie(top_postal_codes['customer_count'], labels=top_postal_codes['customer_zip_code_prefix'], autopct='%1.1f%%', colors=['lightblue'] + ['lightgray'] * (len(top_postal_codes) - 1), startangle=90)
ax4.set_title('Top 10 Postal Codes by Customer Count (Pie Chart)')
ax4.axis('equal')
st.pyplot(fig4)

# Conclusion
st.header("Conclusion")
st.write("""
- Based on the analysis of customer distribution, the city with the highest number of customers is **Sao Paulo**. This indicates that this city is an important target market for the company.
- The postal code with the highest number of customers is **postal code 22790**. This suggests that the area has significant sales potential and should be considered in marketing strategies.
- With this understanding, the company can focus its marketing and sales efforts in areas with a high concentration of customers, as well as consider product development strategies that align with customer preferences in those regions.
""")
