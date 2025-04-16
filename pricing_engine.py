import pandas as pd
def apply_pricing_engine(products_df, sales_df):
    df = pd.merge(products_df, sales_df, on="sku", how="left")
    df["quantity_sold"] = df["quantity_sold"].fillna(0)
    df["old_price"] = df["current_price"].apply(lambda x: f"{x:.2f} INR")

    new_prices = []

    for _, row in df.iterrows():
        current_price = row["current_price"]
        cost_price = row["cost_price"]
        stock = row["stock"]
        quantity_sold = row["quantity_sold"]

        # Rule 1
        if stock < 20 and quantity_sold > 30:
            new_price = current_price * 1.15
        # Rule 2
        elif stock > 200 and quantity_sold == 0:
            new_price = current_price * 0.7
        # Rule 3
        elif stock > 100 and quantity_sold < 20:
            new_price = current_price * 0.9
        else:
            new_price = current_price

        # Rule 4: Minimum Profit Margin
        min_price = cost_price * 1.2
        if new_price < min_price:
            new_price = min_price

        new_price = round(new_price, 2)
        new_prices.append(f"{new_price:.2f} INR")

    df["new_price"] = new_prices
    return df[["sku", "old_price", "new_price"]]
