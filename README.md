# 🧮 Dynamic Pricing Engine with Streamlit

This project is a web-based Dynamic Pricing Engine that automatically adjusts product prices based on real-time inventory and sales performance using a rule-based pricing strategy. Built with Python and Streamlit, it offers an intuitive interface for uploading data, running the pricing logic, and downloading the updated prices.

---

## ✅ Features

- 📤 Upload `products.csv` and `sales.csv`
- ⚖️ Applies prioritized pricing rules
- 🔐 Enforces minimum profit margin (20% above cost)
- 👁️ View updated prices in-browser
- 📥 Download `updated_prices.csv` with final prices

---

## ⚙️ Pricing Rules

Rules are applied in the following order. Only the first applicable rule (from Rule 1–3) is used per product, followed by Rule 4 to ensure profitability.

### Rule 1 – Low Stock, High Demand
- **Condition:** `stock < 20` and `quantity_sold > 30`
- **Action:** Increase price by **15%**

### Rule 2 – Dead Stock
- **Condition:** `stock > 200` and `quantity_sold == 0`
- **Action:** Decrease price by **30%**

### Rule 3 – Overstocked Inventory
- **Condition:** `stock > 100` and `quantity_sold < 20`
- **Action:** Decrease price by **10%**

### Rule 4 – Minimum Profit Constraint (Always Applied)
- **Condition:** `new_price < cost_price * 1.2`
- **Action:** Set price to `cost_price * 1.2`

### 💰 Final Output
- Prices are rounded to **2 decimal places**
- Units (e.g., `INR`) are included for both `old_price` and `new_price`

---

## 🖥️ How to Use the

### ▶️ Run Locally

1. Install dependencies: pip install -r requirements.txt

2. Run the Streamlit app: streamlit run fronted.py

3. In your browser:
   1. Upload products.csv and sales.csv
   2. Click "Run Pricing Engine"
   3. View and download updated_prices.csv
