from flask import Flask, render_template, request
from supabase_client import supabase

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        supabase.table("users").insert(
            {
                "email": email,
                "password_hash": password
            }
        ).execute()
        
        return render_template("succes.html")
    return render_template("register.html")

if __name__=="__main__":
    app.run(debug=True)