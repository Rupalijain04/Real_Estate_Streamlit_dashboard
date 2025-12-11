import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
 

# Load cleaned data
df = pd.read_csv("data/cleaned_data1.csv")


# App title
st.title("Real Estate Investment Dashboard")

# Show full dataset
st.subheader("Dataset Preview")
st.dataframe(df.head())

# City filter
st.subheader("Select City")
city = st.selectbox("Choose a City:", df["City"].unique())

filtered_data = df[df["City"] == city]

st.subheader("Properties in Selected City")
st.dataframe(filtered_data)

# User price input
st.subheader("Enter Property Price")
price = st.number_input("Enter current property price (in lakhs):", min_value=0.0)

# Future price calculation (8% growth for 5 years)
future_price = price * (1.08 ** 5)

st.subheader("Estimated Price After 5 Years")
st.write(f"₹ {round(future_price, 2)} Lakhs")

#  Good / Bad Investment Logic
city_avg_price = filtered_data["Price_in_Lakhs"].mean()

st.subheader("Investment Decision")

if future_price > city_avg_price:
    st.success("✅ This is a GOOD Investment")
else:
    st.error("❌ This is NOT a Good Investment")


# Interactive Price Distribution (Histogram)
fig1 = px.histogram(df, x="Price_in_Lakhs", nbins=30,
                    title="Price Distribution",
                    color_discrete_sequence=["#1f77b4"])
st.plotly_chart(fig1, use_container_width=True)


# Interactive City-wise Average Price Bar Chart
city_price = df.groupby("City")["Price_in_Lakhs"].mean().reset_index()

fig2 = px.bar(city_price.sort_values("Price_in_Lakhs", ascending=False).head(10),
              x="City", y="Price_in_Lakhs",
              title="Top 10 Cities by Average Price",
              color="Price_in_Lakhs",
              color_continuous_scale="Blues")
st.plotly_chart(fig2, use_container_width=True)


# Interactive Property Type Count
fig3 = px.bar(df["Property_Type"].value_counts().reset_index(),
              x="count", y="Property_Type",
              labels={"count": "Property Type", "Property_Type": "count"},
              title="Property Type Distribution",
              color="Property_Type",
              color_continuous_scale="Viridis")
st.plotly_chart(fig3, use_container_width=True)
