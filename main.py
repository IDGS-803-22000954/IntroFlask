from flask import Flask, render_template, request

app=Flask(__name__)
@app.route('/')
def index():
    grupo="IDGS803"
    lista="Juan", "Pedro", "Mario"
    return render_template("index.html", grupo=grupo, lista=lista)

@app.route("/OperasBas")
def operasBas():
    return render_template("OperasBas.html")

@app.route("/cinepolis")
def cinepolis():
    return render_template("cinepolis.html")

@app.route("/resultado", methods=["GET","POST"])
def resultado():
    if request.method == "POST":
        m=request.form.get('calculadora')
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        if m == "suma":
            r=int(num1)+int(num2)
            t='suma'
        if m == "resta":
            r=int(num1)-int(num2)
            t='resta'
        if m == "multiplicacion":
            r=int(num1)*int(num2)
            t='multiplicacion'
        if m == "division":
            r=int(num1)/int(num2)
            t='division'
        return render_template("OperasBas.html", num1=num1, num2=num2, r=r, t=t)

@app.route("/cine", methods=["GET","POST"])
def cine():
    if request.method == 'POST':
        nombre=request.form.get("nombre")
        ccompradores=request.form.get("ccompradores")
        tarjeta=request.form.get("tarjeta")
        cboletas=int(request.form.get("cboletas"))
        if int(cboletas) <= (int(ccompradores)*int(7)):
            if tarjeta == "no":
                if int(cboletas) >= int(5):
                    precio=(int(cboletas)*int(12))*float(0.85)
                    r="Hola {}, tu precio es de {} pesos".format(nombre, precio)
                elif int(cboletas) >=3:
                    precio=(int(cboletas)*int(12))*float(0.90)
                    r="Hola {}, tu precio es de {} pesos".format(nombre, precio)
                else:
                    precio=int(cboletas)*int(12)
                    r="Hola {}, tu precio es de {} pesos".format(nombre, precio)
            elif tarjeta == "si":
                if int(cboletas) >= int(5):
                    precio=((int(cboletas)*int(12))*float(0.75))
                    r="Hola {}, tu precio es de {} pesos".format(nombre, precio)
                elif int(cboletas) >= int(3):
                    precio=((int(cboletas)*int(12))*float(0.80))
                    r="Hola {}, tu precio es de {} pesos".format(nombre, precio)
                else:
                    precio=(int(cboletas)*int(12))*float(0.90)
                    r="Hola {}, tu precio es de {} pesos".format(nombre, precio)
        else:
            r="La cantidad de boletas excede a la de compradores"
        return render_template("cinepolis.html", r=r) 

@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route("/hola")
def hola():
    return "Simon"

@app.route("/user/<string:user>")
def user(user):
    return f"Hola {user}!!!"

@app.route("/numero/<int:n>")
def numero(n):
    return "Numero: {}".format(n)

@app.route("/user/<string:user>/<int:id>")
def username(user,id):
    return f"Hola {user} ID: {id}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return "La suma es: {}".format(n1+n2)

@app.route("/default")
@app.route("/default/<string:nom>")
def func(nom='pedro'):
    return 'El nombre de Nom es '+nom

@app.route("/form1")
def form1():
    return '''
    <form>
    <label>Nombre</label>
    <input type"text" name="nombre" placeholder="Nombre">
    </br>
    <label>Nombre</label>
    <input type"text" name="nombre" placeholder="Nombre">
    </br>
    <label>Nombre</label>
    <input type"text" name="nombre" placeholder="Nombre">
    </br>
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True, port=8081)