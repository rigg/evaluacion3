from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods = ['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])
        promedio = float((nota1 + nota2 + nota3) / 3)
        if(asistencia >= 75 and promedio >= 4.0 ):
            estado = 'APROBADO'
        else:
            estado = 'REPROBADO'

        return render_template('ejercicio1.html', promedio=promedio, nota1=nota1, nota2=nota2, nota3=nota3, estado=estado)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods = ['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']
        nombreMayor = ''
        cantidadCaracteres = 0

        lista1 = list(nombre1)
        lista2 = list(nombre2)
        lista3 = list(nombre3)

        if len(lista1) > len(lista2) and len(lista1) > len(lista2):
            nombreMayor = nombre1
            cantidadCaracteres = len(lista1)
        elif len(lista2) > len(lista1) and len(lista2) > len(lista3):
            nombreMayor = nombre2
            cantidadCaracteres = len(lista2)
        elif len(lista3) > len(lista1) and len(lista3) > len(lista2):
            nombreMayor = nombre3
            cantidadCaracteres = len(lista3)

        return render_template('ejercicio2.html', nombre1=nombre1, nombre2=nombre2, nombre3=nombre3, nombreMayor=nombreMayor, cantidadCaracteres=cantidadCaracteres)
    return render_template('ejercicio2.html')




if __name__ == '__main__':
    app.run(debug=True)
