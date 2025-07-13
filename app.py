from flask import Flask, render_template, redirect, url_for,request # type: ignore
app=Flask(__name__)

#app route for home page

# In-memory user credentials (for demo purposes)
valid_username = "heidi"
valid_password = "123"

# Route to display the login form
@app.route('/')
def main():
    return render_template("login.html")

# Route to handle login form submission
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    
    # Check if credentials match
    if username == valid_username and password == valid_password:
        return redirect(url_for("home"))
    else:
        return "Invalid credentials, please try again."

@app.route('/home.html') 
def home():
    return render_template('home.html')

#app route for about page

@app.route('/about.html')
def about():
    return render_template('about.html')

#app route for courses page

@app.route('/courses.html')
def courses():
    return render_template('courses.html')

#app route for blog page

@app.route('/blog.html')
def blog():
    return render_template('blog.html')

#app route for contact page

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

if __name__=='__main__':
    app.run(debug=True)