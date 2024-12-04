from flask import Flask, render_template, session, request, redirect, url_for, flash
from service.EarringService import EarringService
from service.UserService import UserService

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with a strong secret key in production

earring_service = EarringService()
userService = UserService()


# Define a hardcoded password (for demonstration)

@app.before_request
def initialize_cart():
    if 'cart' not in session:
        session['cart'] = []


# Force login check
#@app.before_request
#def force_login():
    #if 'user_email' not in session and request.endpoint not in ['login', 'logout']:
       # return redirect(url_for('login'))  # Redirect to log in if user is not logged in


# Login route with hardcoded password
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Extract email and password from form data
        email = request.form.get('emailField')
        password = request.form.get('passwordField')

        user = userService.get_user_by_email(email)

        # Check if the provided password matches the hardcoded password
        if user is not None:
            if password == user.password:
                session['user_email'] = email  # Store the user's email in session

                if user.position:
                    flash('Login successful!', 'success')
                    return redirect(url_for('show_earrings'))  # Redirect to the earrings page

                else:
                    return render_template("admin.html")

            else:
                flash('Invalid password.', 'error')
        else:
            flash('Invalid email or password', 'error')

    # Render the login page if it's a GET request or if the POST fails
    return render_template('login.html')


# Logout route
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_email', None)  # Remove the user session
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))  # Redirect to login page after logout


# Show earrings page


# Show earring details page
@app.route('/earring/<int:earring_id>')
def show_earring(earring_id):
    earring = earring_service.get_earring_details(earring_id)
    if earring:
        return render_template('earring_detail.html', earring=earring)
    else:
        return "Earrings not found", 404


@app.route('/earrings')
def show_earrings():
    earrings = earring_service.get_all_earrings()
    return render_template('earring_list.html', earrings=earrings)


# Add to cart route
@app.route('/add_to_cart/<int:earring_id>', methods=['POST'])
def add_to_cart(earring_id):
    earring = earring_service.get_earring_details(earring_id)
    if not earring:
        flash('Earrings not found.', 'error')
        return redirect(url_for('show_earrings'))

    cart = session.get('cart', [])
    if earring_id in cart:
        flash('Earrings are already in your cart.', 'info')
    else:
        cart.append(earring_id)
        session['cart'] = cart
        flash('Earrings added to your cart.', 'success')

    return redirect(url_for('show_earrings', earring_id=earring_id))


# View cart route
@app.route('/cart')
def view_cart():
    cart = session.get('cart', [])
    earrings = [earring_service.get_earring_details(earring_id) for earring_id in cart]
    earrings = [earring for earring in earrings if earring is not None]  # Filter out None values
    return render_template('cart.html', earrings=earrings)


# Remove from cart route
@app.route('/remove_from_cart/<int:earring_id>', methods=['POST'])
def remove_from_cart(earring_id):
    cart = session.get('cart', [])
    if earring_id in cart:
        cart.remove(earring_id)
        session['cart'] = cart
        flash('Earrings removed from your cart.', 'success')
    else:
        flash('Earrings not found in your cart.', 'error')
    return redirect(url_for('view_cart'))


if __name__ == '__main__':
    app.run(debug=True)
