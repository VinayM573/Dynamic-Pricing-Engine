import streamlit as st
from pricing_engine import apply_pricing_engine
import pandas as pd
s
st.set_page_config(page_title="Dynamic Pricing Engine", layout="centered")

st.title("🧮 Dynamic Pricing Engine")
st.write("Automatically adjust product prices based on inventory and sales data.")

# Upload CSV files
products_file = st.file_uploader("📦 Upload products.csv", type="csv")
sales_file = st.file_uploader("📈 Upload sales.csv", type="csv")

if products_file and sales_file:
    products_df = pd.read_csv(products_file)
    sales_df = pd.read_csv(sales_file)

    st.subheader("Preview: Products Data")
    st.dataframe(products_df)

    st.subheader("Preview: Sales Data")
    st.dataframe(sales_df)

    if st.button("⚙️ Run Pricing Engine"):
        result_df = apply_pricing_engine(products_df, sales_df)
        st.success("✅ Pricing Engine Applied Successfully!")
        st.subheader("📤 Updated Prices")
        st.dataframe(result_df)

        # Download
        csv = result_df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="⬇️ Download updated_prices.csv",
            data=csv,
            file_name="updated_prices.csv",
            mime="text/csv"
        )
