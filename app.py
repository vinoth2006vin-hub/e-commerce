import streamlit as st

# -----------------------------
# Page Settings
# -----------------------------
st.set_page_config(
    page_title="AI E-Commerce Customer Support",
    page_icon="🛒"
)

st.title("🛒 AI E-Commerce Customer Support Agent")

st.write(
    "Welcome! I can help with products, orders, returns, and recommendations."
)


# -----------------------------
# Product Database
# -----------------------------
products = [
    # Mobiles
    {
        "name": "Samsung Galaxy A55",
        "category": "Mobile",
        "price": 28999,
        "stock": 15
    },
    {
        "name": "Samsung Galaxy S24",
        "category": "Mobile",
        "price": 74999,
        "stock": 8
    },
    {
        "name": "iPhone 15",
        "category": "Mobile",
        "price": 59999,
        "stock": 12
    },
    {
        "name": "iPhone 15 Pro",
        "category": "Mobile",
        "price": 99999,
        "stock": 5
    },
    {
        "name": "Redmi Note 14",
        "category": "Mobile",
        "price": 17999,
        "stock": 20
    },
    {
        "name": "OnePlus 13",
        "category": "Mobile",
        "price": 69999,
        "stock": 7
    },

    # Laptops
    {
        "name": "HP Pavilion 15",
        "category": "Laptop",
        "price": 54999,
        "stock": 8
    },
    {
        "name": "Dell Inspiron 14",
        "category": "Laptop",
        "price": 49999,
        "stock": 10
    },
    {
        "name": "Lenovo IdeaPad Slim 5",
        "category": "Laptop",
        "price": 57999,
        "stock": 6
    },
    {
        "name": "ASUS Vivobook 15",
        "category": "Laptop",
        "price": 52999,
        "stock": 9
    },
    {
        "name": "Acer Aspire 5",
        "category": "Laptop",
        "price": 44999,
        "stock": 11
    },

    # Headphones
    {
        "name": "Sony WH-1000XM5",
        "category": "Headphones",
        "price": 29999,
        "stock": 5
    },
    {
        "name": "boAt Rockerz 550",
        "category": "Headphones",
        "price": 1999,
        "stock": 25
    },
    {
        "name": "JBL Tune 770NC",
        "category": "Headphones",
        "price": 5999,
        "stock": 15
    },

    # Smart Watches
    {
        "name": "Apple Watch Series 10",
        "category": "Smart Watch",
        "price": 46999,
        "stock": 6
    },
    {
        "name": "Samsung Galaxy Watch 7",
        "category": "Smart Watch",
        "price": 29999,
        "stock": 8
    },
    {
        "name": "Noise ColorFit Pro",
        "category": "Smart Watch",
        "price": 2999,
        "stock": 20
    },

    # Tablets
    {
        "name": "Apple iPad 10th Gen",
        "category": "Tablet",
        "price": 34999,
        "stock": 10
    },
    {
        "name": "Samsung Galaxy Tab S9",
        "category": "Tablet",
        "price": 72999,
        "stock": 5
    },
    {
        "name": "Redmi Pad Pro",
        "category": "Tablet",
        "price": 24999,
        "stock": 12
    },

    # Accessories
    {
        "name": "Apple AirPods Pro",
        "category": "Accessories",
        "price": 24999,
        "stock": 7
    },
    {
        "name": "Samsung 25W Charger",
        "category": "Accessories",
        "price": 1299,
        "stock": 30
    },
    {
        "name": "Logitech Wireless Mouse",
        "category": "Accessories",
        "price": 1499,
        "stock": 25
    },

    # Cameras
    {
        "name": "Canon EOS 1500D",
        "category": "Camera",
        "price": 42999,
        "stock": 4
    },
    {
        "name": "Sony Alpha A6400",
        "category": "Camera",
        "price": 72999,
        "stock": 3
    },
    {
       "name": "Sony Alpha A6402",
       "category": "Camera",
       "price": 745,
       "stock": 8 
    }

]


# -----------------------------
# Product Search Tool
# -----------------------------
def search_products(query):

    results = []

    query = query.lower()

    for product in products:

        if (
            query in product["name"].lower()
            or query in product["category"].lower()
        ):
            results.append(product)

    return results


# -----------------------------
# Product Search UI
# -----------------------------
st.subheader("🔎 Product Search")

query = st.text_input(
    "Enter a product or category"
)

if st.button("Search Products"):

    results = search_products(query)

    if results:

        for product in results:

            st.write(
                f"### 🛍️ {product['name']}"
            )

            st.write(
                f"Category: {product['category']}"
            )

            st.write(
                f"Price: ₹{product['price']}"
            )

            st.write(
                f"Available Stock: {product['stock']}"
            )

            st.divider()

    else:

        st.warning(
            "No products found."
        )