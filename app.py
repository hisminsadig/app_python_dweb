from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Mi Página de Inicio</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 80px;
                background-color: #f4f4f9;
                color: #333;
            }
            h1 { color: #0066cc; }
            .caja {
                background: white;
                padding: 30px;
                border-radius: 10px;
                display: inline-block;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            }
        </style>
    </head>
    <body>
        <div class="caja">
            <h1>¡Bienvenido a mi proyecto!</h1>
            <p>Esta página de inicio fue creada con Python y subida desde Google Colab.</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
