from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    name = "Purva"
    skills = ["Python", "Flask", "Jenkins", "Git", "Docker"]
    return render_template("index.html", name=name, skills=skills)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=50005)