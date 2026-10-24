from flask import Flask, render_template, request
#from sorteador import rolar_dados
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():
    #
    return render_template("teste.html")

if __name__ == "__main__":
    app.run(debug=True)