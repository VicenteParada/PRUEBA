from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

class Conductor:
    def __init__(self, id_conductor, nombre_conductor, cantidad_excesos):
        self.id_conductor = id_conductor
        self.nombre_conductor = nombre_conductor
        self.cantidad_excesos = cantidad_excesos

class Reinstructor:
    def __init__(self, id_reinstructor, nombre_reinstructor, nivel_reinstructor, correo_reinstructor):
        self.id_reinstructor = id_reinstructor
        self.nombre_reinstructor = nombre_reinstructor
        self.nivel_reinstructor = nivel_reinstructor
        self.correo_reinstructor = correo_reinstructor

class Reinstruccion:
    def __init__(self, id_reinstruccion, reinstructor, conductor, fecha_asignacion=None, realizado_bool=False):
        self.id_reinstruccion = id_reinstruccion
        self.reinstructor = reinstructor
        self.conductor = conductor
        self.fecha_asignacion = fecha_asignacion or datetime.now().strftime("%d/%m/%Y")
        self.realizado_bool = realizado_bool

@app.route('/')
def index():
    conductor = Conductor(1, "Jaime Lique Tinte", 5)
    reinstructor = Reinstructor(1, "Luis Trujillo", "Tipo 1", "luis.trujillo@example.com")
    reinstruccion = Reinstruccion(1, reinstructor, conductor)

    reinstrucciones = [reinstruccion]

    return render_template('index.html', reinstrucciones=reinstrucciones)

if __name__ == "__main__":
    app.run(debug=True)
