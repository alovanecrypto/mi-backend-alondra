import os
from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Promedio Primer Parcial</title>
<style>
    body { 
        background-color: #f0f4f8; 
        font-family: Arial, sans-serif; 
        display: flex; 
        justify-content: center; 
        padding: 20px;
        margin:0;
    }
    .card {
        background: white;
        width: 100%;
        max-width: 450px;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    h1 { text-align:center; color: #2c3e50; font-size: 1.4rem; }
    h2 { text-align:center; color: #3498db; font-size: 1.1rem; font-weight: normal; }
    .presentacion {
        background: #eaf2f8;
        border-left: 4px solid #3498db;
        padding: 10px 15px;
        border-radius: 8px;
        margin-bottom: 20px;
        text-align: center;
    }
    label { display: block; margin-top: 12px; font-weight: bold; color: #34495e; font-size: 0.9rem; }
    input {
        width: 100%;
        padding: 10px;
        margin-top: 4px;
        border: 1px solid #d5dbdb;
        border-radius: 8px;
        box-sizing: border-box;
        background-color: #fcfefe;
    }
    button {
        width: 100%;
        padding: 12px;
        background-color: #3498db;
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: bold;
        font-size: 1rem;
        margin-top: 20px;
        cursor: pointer;
    }
    button:hover { background-color: #2e86c1; }
    .resultado {
        margin-top: 20px;
        background-color: #d4efdf;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        font-weight: bold;
        color: #1e8449;
        font-size: 1.2rem;
    }
</style>
</head>
<body>
<div class="card">
    <h1>Calificaciones 1er Parcial</h1>
    
    <div class="presentacion">
        <strong>Pantalla de Presentación</strong><br>
        Alumno: {{ nombre_completo }}<br>
        Fecha: 14-Sep-26<br>
        Ejercicio de Python / Flask
    </div>

    <form method="POST">
        <label>Nombre completo del alumno:</label>
        <input type="text" name="nombre" value="{{ nombre_completo }}" required>

        <label>Matemáticas:</label>
        <input type="number" step="0.1" min="0" max="10" name="m1" required>

        <label>Inglés:</label>
        <input type="number" step="0.1" min="0" max="10" name="m2" required>

        <label>Comunicación:</label>
        <input type="number" step="0.1" min="0" max="10" name="m3" required>

        <label>submódulo I:</label>
        <input type="number" step="0.1" min="0" max="10" name="m4" required>

        <label>Submódulo II:</label>
        <input type="number" step="0.1" min="0" max="10" name="m5" required>
        
        <label> lenguaje y comunicacion:</label>
        <input type = "number" step = "0.1"
min = "0" max ="10" name ="m6" required>

        <button type="submit">Calcular Promedio</button>
    </form>

    {% if promedio is not none %}
    <div class="resultado">
        Hola {{ nombre_completo }}<br>
        Tu Promedio del Primer Parcial es: {{ promedio }}
    </div>
    {% endif %}
</div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    # CAMBIA TU NOMBRE AQUÍ
    nombre_default = "Pon aquí tu Nombre Completo"
    promedio = None
    nombre_completo = nombre_default

    if request.method == 'POST':
        nombre_completo = request.form.get('nombre')
        m1 = float(request.form.get('m1') or 0)
        m2 = float(request.form.get('m2') or 0)
        m3 = float(request.form.get('m3') or 0)
        m4 = float(request.form.get('m4') or 0)
        m5 = float(request.form.get('m5') or 0)
        m6 = float(request.form.get('m6') or 0)
        promedio = round((m1 + m2 + m3 + m4 + m5 + m6) / 6,2)

  # --- ESTO ES LO QUE LO GUARDA EN TXT ---
        with open("calificaciones.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"----------------------------------\n")
            archivo.write(f"Alumno: {nombre_completo}\n")
            archivo.write(f"Matemáticas: {m1}\n")
            archivo.write(f"Inglés: {m2}\n")
            archivo.write(f"Sistema terreste: {m3}\n")
            archivo.write(f"submódulo I: {m4}\n")
            archivo.write(f"Submódulo II: {m5}\n")
            archivo.write(f"lenguaje y comunicacion: {m6}\n")
            archivo.write(f"Promedio: {promedio}\n")
            archivo.write(f"----------------------------------\n\n")
            
    return render_template_string(HTML, promedio=promedio, nombre_completo=nombre_completo)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
