from flask import Flask, render_template, request
from flask_assets import Environment, Bundle
#from sorteador import rolar_dados
app = Flask(__name__)

assets = Environment(app)

scss = Bundle(
    'css/d20.css',
    filters='pyscss',
    output='css/d20.css'
)

assets.register('scss_all', scss)

@app.route("/", methods=["GET", "POST"])
def inicio():
    return render_template("teste.html")
@app.route("/char_prof")
def eleccion():
    return render_template("characters_profile.html")


if __name__ == "__main__":
    app.run(debug=True)