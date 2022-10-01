from flask import Flask, render_template
app = Flask(__name__)

class Customer:
    def sign_up(self):
        name=input('enter your name:')
        address=input('enter your address:')
        password=input('enter password:')
        account_n0=input('enter your account no:')
        return name,address,password,account_n0

    @app.route('/signup')
    def work():
        k=Customer.sign_up()
        return render_template('signup.html',k=k)

class Abc:

    @app.route('/')
    @app.route('/home')
    def home_page():
       return render_template('home.html')


    @app.route('/market')
    def market_page():
        items = [
            {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
            {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
            {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
        ]
        return render_template('market.html', items=items)



    app.run(debug=True)
a=Abc()

