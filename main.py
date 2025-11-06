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

@app.route('/nombres')
def ejercicio2():
    return render_template('form_nombres.html')

if __name__ == '__main__':
    app.run(debug=True)
