from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Base de datos en memoria
productos = {}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        producto = request.form.get("producto")
        precio = request.form.get("precio")
        if producto and precio:
            try:
                productos[producto] = float(precio)
            except ValueError:
                pass  # Ignorar si no es un número

    busqueda = request.args.get("busqueda")
    resultados = {k: v for k, v in productos.items() if busqueda.lower() in k.lower()} if busqueda else productos
    return render_template("index.html", productos=resultados)

@app.route("/eliminar", methods=["POST"])
def eliminar():
    producto = request.form.get("producto")
    if producto in productos:
        del productos[producto]
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)