from flask import Flask, render_template
from getData.get import get_data

app = Flask(__name__)

fuels_and_price = get_data()#list[tuples] -> (fuel, price)

@app.route('/')
def home():
    return render_template('index.html', data=fuels_and_price)

if __name__ == "__main__":
    app.run(debug=True)