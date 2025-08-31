from flask import Flask, request, redirect, url_for, session, Response

app = Flask(__name__)
app.secret_key = "supersecret"

# homepage login page
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "123":
            session["user"] = username #store in session
            return redirect(url_for("welcome"))
        else:
            return Response("In-valid credentials.Try agains", mimetype="text/plan")
 
    return'''
            <h2> Login Page</h2>
            <form.method="POST">
            username: <input type="text"  name="username"><br>
            password: <input type="text"   name="password"><br>
            <input type="submit" values="Login"
            </from>

'''
#welcome page(after/ login)
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
        <h2>Welcome, {session["user"]}!</h2>
        <a href={url_for('login')}>logout</a>
    '''
    return redirect(url_for("login"))

#logout route
@app.route("/logout")
def logout():
    session.pop("user")   #session["user"]="khushi"
    return redirect(url_for("login"))
