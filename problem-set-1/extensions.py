"""
Aunque Windows y macOS a veces los ocultan, la mayoría de los archivos tienen extensiones de archivo, un sufijo que comienza con un punto (.) al final de su nombre.  Por ejemplo, los nombres de archivo para GIF terminan en .gif y los nombres de archivo para JPEG terminan en .jpg o .jpeg.  Cuando hace doble clic en un archivo para abrirlo, su computadora usa su extensión de archivo para determinar qué programa iniciar.

Los navegadores web, por el contrario, se basan en tipos de medios, anteriormente conocidos como tipos MIME, para determinar cómo mostrar los archivos que viven en la web.  Cuando descarga un archivo de un servidor web, ese servidor envía un encabezado HTTP, junto con el propio archivo, que indica el tipo de medio del archivo.  Por ejemplo, el tipo de medio para un GIF es imagen/gif y el tipo de medio para un JPEG es imagen/jpeg.  Para determinar el tipo de medio para un archivo, un servidor web normalmente busca la extensión del archivo, mapeando una a la otra.

Consulte developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types para conocer los tipos comunes.

En un archivo llamado extensions.py, implemente un programa que solicite al usuario el nombre de un archivo y luego muestre el tipo de medio de ese archivo si el nombre del archivo termina, sin distinción de mayúsculas y minúsculas.
"""
def media_types():
    images = ['gif', 'jpg', 'jpeg', 'png']
    app = ['pdf', 'zip']

    file = input('File name: ').strip().lower().split('.')
    type_file = len(file) - 1

    types_matriz = [images, app, ['txt']]


    if len(file) < 2:
        print(f'application/octet-stream')
    else:
        for i in range(len(types_matriz)):

            type_located = False

            for j in range(len(types_matriz[i])):
                if file[type_file] == types_matriz[i][j]:
                    type_located = True

                    if i == 0:
                        if file[type_file] == 'jpg':
                            print(f'image/jpeg')
                        else:
                            print(f'image/{file[type_file]}')
                    elif i == 1:
                        print(f'application/{file[type_file]}')
                    elif i == 2:
                        print(f'text/plain')

                    return

        if not type_located:
            print(f'application/octet-stream')


media_types()