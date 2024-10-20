from flask import Flask, render_template

# Initialize the Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

# Additional routes for other pages
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5002)
