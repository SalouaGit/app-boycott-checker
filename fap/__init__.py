from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_product_info(product_name):
    try:
        conn = sqlite3.connect('/var/www/fap/fap/products.db')
        c = conn.cursor()
        c.execute("SELECT boycotted, description FROM products WHERE name=?", (product_name,))
        result = c.fetchone()
        conn.close()
        if result is not None:
            return {"boycotted": bool(result[0]), "description": result[1]}
        return None
    except Exception as e:
        app.logger.error(f"Error getting product info: {e}")
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        product_name = request.form.get('product_name').lower()
        return redirect(url_for('result', product_name=product_name))
    return render_template('index.html')

@app.route('/result/<product_name>')
def result(product_name):
    product_info = get_product_info(product_name)
    return render_template('result.html', product_name=product_name, product_info=product_info)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/why_boycott')
def why_boycott():
    return render_template('why_boycott.html')

if __name__ == '__main__':
    app.run()

