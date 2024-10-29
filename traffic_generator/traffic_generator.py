import random
import time
import string
import pandas as pd
import requests

# Leer el dataset desde el archivo CSV
data = pd.read_csv('Data2_SD.csv', header=None)

product_names = data.iloc[0].dropna().tolist()
prices = data.iloc[1].dropna().tolist()
payment_gateways = data.iloc[2].dropna().tolist()
card_brands = data.iloc[3].dropna().tolist()
banks = data.iloc[4].dropna().tolist()
shipping_regions = data.iloc[5].dropna().tolist()

def simulate_order():
    index = random.randint(0, len(product_names) - 1)
    random_string = ''.join(random.choices(string.ascii_letters, k=10))
    product_name = product_names[index]
    price = prices[index]
    payment_gateway = random.choice(payment_gateways)
    card_brand = random.choice(card_brands)
    bank = random.choice(banks)
    shipping_direction = f"{random.choice(shipping_regions)}_{random_string}"
    email = 'testsd454@gmail.com'
    return {
        "product_name": product_name,
        "price": price,
        "payment_gateway": payment_gateway,
        "card_brand": card_brand,
        "bank": bank,
        "shipping_direction": shipping_direction,
        "email": email
    }

def generate_orders():
    time.sleep(50)
    while True:
        # Simular un pedido
        order = simulate_order()
        # Enviar la petición al cliente gRPC
        response = requests.post("http://grpc_client:5008/send_order", json=order)
        response_data = response.json()
        order_id = response_data.get("id")
        print(f"ID del pedido es: {order_id}")
        time.sleep(2)

if __name__ == '__main__':
    generate_orders()
