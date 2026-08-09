from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 1. PANTALLA DE REGISTRO / LOGIN
@app.route('/', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        usuario = request.form['username']
        # Redirige al menú principal pasando el nombre
        return redirect(url_for('menu', jugador=usuario))
    return render_template('registro.html')

# 2. PANTALLA DEL MENÚ PRINCIPAL
@app.route('/menu')
def menu():
    jugador = request.args.get('jugador', 'Estudiante')
    return render_template('menu.html', jugador=jugador)

# 3. PANTALLA DEL MAPA INTERACTIVO
@app.route('/mapa')
def mapa():
    jugador = request.args.get('jugador', 'Estudiante')
    # Flask recibe el nombre de la imagen del avatar seleccionado
    avatar = request.args.get('avatar', 'char1.png') 
    return render_template('mapa.html', jugador=jugador, avatar=avatar)

if __name__ == '__main__':
    app.run(debug=True)