# main.py
from flask import Flask, render_template
from faker import Faker
import random

app = Flask(__name__)
fake = Faker()

@app.route('/')
def index():
    # Generar datos simulados de ventas
    num_sales = 100
    sales_data = [{'date': fake.date_this_year(), 'amount': round(random.uniform(100, 1000), 2)} for _ in range(num_sales)]
    
    # Calcular algunas estadísticas básicas
    total_sales = sum(sale['amount'] for sale in sales_data)
    avg_sales = total_sales / num_sales
    max_sales = max(sales_data, key=lambda x: x['amount'])['amount']
    min_sales = min(sales_data, key=lambda x: x['amount'])['amount']

    # Renderizar la plantilla HTML y pasar los datos como contexto
    return render_template('index.html', total_sales=total_sales, avg_sales=avg_sales, max_sales=max_sales, min_sales=min_sales)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

