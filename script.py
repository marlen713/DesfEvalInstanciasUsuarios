import json
from usuario import Usuario


usuarios = []

with open('usuarios.txt', 'r') as file:
    for line in file:
        try:
            data = json.loads(line)
            usuario = Usuario(data['nombre'], data['apellido'], data['email'], data['genero'])
            usuarios.append(usuario)
        except Exception as e:
            with open('error.log', 'a') as errorfile:
                errorfile.write(f'Error al procesar línea: {line}\n')
                errorfile.write(f'Error: {str(e)}\n')

# Verificar que las instancias de Usuario se han creado correctamente
for usuario in usuarios:
    print(f'Usuario: {usuario.nombre} {usuario.apellidos} - Email: {usuario.email} - Género: {usuario.genero}')