import webbrowser
from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_CODE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ficha de Identificación</title>
    <style>
        body {
            background-color: #2B1B3D;
            color: #FFFFFF;
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            padding: 15px;
            margin: 0;
        }
        .card {
            background: linear-gradient(to bottom, #0077FE, #6A0DAD);
            width: 100%;
            max-width: 420px;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
            box-sizing: border-box;
        }
        .header-top {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 12px;
            margin-bottom: 15px;
        }
        .logo {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            object-fit: cover;
            border: 2px solid #E2D0F9;
        }
        h2 {
            margin: 0;
            color: #FFFFFF;
            font-size: 1.5rem;
            font-weight: bold;
            text-transform: uppercase;
            text-shadow: 1px 1px 4px rgba(0,0,0,0.4);
        }
        .top-section {
            display: flex;
            gap: 12px;
        }
        .inputs-left {
            flex: 1;
        }
        .photo-container {
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .photo-box {
            width: 95px;
            height: 115px;
            border: 2px dashed #D1B3E0;
            background-color: rgba(0, 0, 0, 0.2);
            display: flex;
            align-items: center;
            justify-content: center;
            color: #D1B3E0;
            border-radius: 8px;
            font-size: 0.8rem;
            overflow: hidden;
            margin-bottom: 6px;
        }
        .photo-box img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        .file-input {
            width: 95px;
            font-size: 0.65rem;
            color: #E2D0F9;
        }
        label {
            display: block;
            font-size: 0.8rem;
            font-weight: bold;
            margin-top: 8px;
            margin-bottom: 2px;
            color: #FFFFFF;
        }
        input[type="text"], input[type="number"], input[type="date"] {
            width: 100%;
            padding: 8px;
            border: none;
            border-radius: 6px;
            background-color: #F3E9F8;
            color: #000;
            box-sizing: border-box;
            font-size: 0.9rem;
        }
        button {
            width: 100%;
            padding: 12px;
            background-color: #25004D;
            color: white;
            border: none;
            border-radius: 8px;
            font-weight: bold;
            font-size: 1rem;
            margin-top: 18px;
            cursor: pointer;
        }
        .alert {
            background-color: #25833e;
            color: white;
            padding: 10px;
            border-radius: 6px;
            margin-bottom: 15px;
            text-align: center;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>
    <div class="card">
        <div class="header-top">
            <img class="logo" src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png" alt="Logo">
            <h2>Ficha de Identificación</h2>
        </div>
        
        {% if mensaje %}
            <div class="alert">{{ mensaje }}</div>
        {% endif %}

        <form method="POST">
            <div class="top-section">
                <div class="inputs-left">
                    <label>AP (Apellido Paterno):</label>
                    <input type="text" name="ap" required>

                    <label>AM (Apellido Materno):</label>
                    <input type="text" name="am">

                    <label>N (Nombre):</label>
                    <input type="text" name="nombre" required>
                </div>
                
                <div class="photo-container">
                    <div class="photo-box" id="preview-box">
                        <span id="placeholder-text">Sin Foto</span>
                        <img id="img-preview" style="display:none;" alt="Foto">
                    </div>
                    <input type="file" accept="image/*" class="file-input" onchange="mostrarImagen(event)">
                </div>
            </div>

            <label>Edad:</label>
            <input type="number" name="edad">

            <label>Fecha de nacimiento:</label>
            <input type="date" name="fecha">

            <label>Grado de estudios:</label>
            <input type="text" name="estudios">

            <button type="submit">Guardar Ficha</button>
        </form>
    </div>

    <script>
        function mostrarImagen(event) {
            const input = event.target;
            if (input.files && input.files[0]) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    const img = document.getElementById('img-preview');
                    const placeholder = document.getElementById('placeholder-text');
                    img.src = e.target.result;
                    img.style.display = 'block';
                    placeholder.style.display = 'none';
                }
                reader.readAsDataURL(input.files[0]);
            }
        }
    </script>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    mensaje = None
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        ap = request.form.get('ap')
        mensaje = f"¡Ficha de {nombre} {ap} guardada!"
    return render_template_string(HTML_CODE, mensaje=mensaje)

if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:5000")
    app.run(port=5000)
