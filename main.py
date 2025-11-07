from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/notas', methods=['GET', 'POST'])
def ejercicio1():
    resultado = None
    promedio = None
    estado = None

    # Valores iniciales vacíos
    nota1 = ""
    nota2 = ""
    nota3 = ""
    asistencia = ""

    if request.method == 'POST':
        nota1 = request.form['nota1']
        nota2 = request.form['nota2']
        nota3 = request.form['nota3']
        asistencia = request.form['asistencia']
        try:
            promedio = round((float(nota1) + float(nota2) + float(nota3)) / 3, 2)
            estado = "Aprobado" if promedio >= 40 and float(asistencia) >= 75 else "Reprobado"
            resultado = True
        except Exception:
            resultado = False

    return render_template('form_notas.html',
                           resultado=resultado,
                           promedio=promedio,
                           estado=estado,
                           nota1=nota1,
                           nota2=nota2,
                           nota3=nota3,
                           asistencia=asistencia)



@app.route('/nombres', methods=['GET', 'POST'])
def ejercicio2():
    resultado = None
    nombres_largos = []
    cantidad = 0

    nombre1 = ""
    nombre2 = ""
    nombre3 = ""

    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        nombres = [nombre1, nombre2, nombre3]
        max_len = max(len(nombre) for nombre in nombres)
        # Lista con todos los nombres que tienen la cantidad máxima de letras
        nombres_largos = [nombre for nombre in nombres if len(nombre) == max_len]
        cantidad = max_len
        resultado = True

    return render_template('form_nombres.html',
                           resultado=resultado,
                           nombre1=nombre1,
                           nombre2=nombre2,
                           nombre3=nombre3,
                           nombres_largos=nombres_largos,
                           cantidad=cantidad)

if __name__ == '__main__':
    app.run(debug=True)
