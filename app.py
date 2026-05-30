from flask import Flask

# Inicializa a aplicação Flask
app = Flask(__name__)

# Define a rota para a página principal
@app.route("/")
def index():
    return "Olá! Meu servidor Flask está funcionando!"

# Inicia o servidor local
if __name__ == "__main__":
    app.run(debug=True)
