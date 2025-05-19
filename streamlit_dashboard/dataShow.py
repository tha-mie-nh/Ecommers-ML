import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
file_path = r"C:\Users\Admin\Desktop\E_commerce_proj\data\raw\checkdata.csv"
df = pd.read_csv(file_path)

# Streamlit App
st.title("E-commerce Sales Dashboard")

# Show dataset
if st.checkbox("Show Raw Data"):
    st.write(df.head())

# Sales Trend Over Time
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df_sales = df.groupby(df['Date'].dt.to_period('M'))['Amount'].sum().reset_index()
df_sales['Date'] = df_sales['Date'].astype(str)

st.subheader("Monthly Sales Trend")
fig, ax = plt.subplots()
ax.plot(df_sales['Date'], df_sales['Amount'], marker='o', linestyle='-')
plt.xticks(rotation=45)
st.pyplot(fig)

# Sales by Category
st.subheader("Sales by Category")
df_category = df.groupby('Category')['Amount'].sum().reset_index()
fig, ax = plt.subplots()
ax.bar(df_category['Category'], df_category['Amount'])
plt.xticks(rotation=45)
st.pyplot(fig)

# Summary Statistics
st.subheader("Summary Statistics")
total_sales = df['Amount'].sum()
total_orders = df['Order ID'].nunique()
st.metric("Total Revenue", f"₹ {total_sales:,.2f}")
st.metric("Total Orders", total_orders)

# Relationship Between Variables
st.subheader("Relationship Between Variables")

# Scatter plot: Amount vs. Quantity
fig, ax = plt.subplots()
sns.scatterplot(x=df['Qty'], y=df['Amount'], ax=ax)
ax.set_xlabel("Quantity")
ax.set_ylabel("Amount")
st.pyplot(fig)

# Box plot: Amount by Fulfilment Type
fig, ax = plt.subplots()
sns.boxplot(x=df['Fulfilment'], y=df['Amount'], ax=ax)
ax.set_xlabel("Fulfilment Type")
ax.set_ylabel("Amount")
st.pyplot(fig)

# Correlation Heatmap
st.subheader("Correlation Heatmap")
fig, ax = plt.subplots()
sns.heatmap(df[['Amount', 'Qty']].corr(), annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)

