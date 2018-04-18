# Python Ecuador

Código fuente del sitio de Python Ecuador

# Colaborar

Pull requests son bienvenidos! Recién estamos empezando,
así que hay mucho por hacer.

Puedes mirar en los issues abiertos para buscar tareas por hacer <https://github.com/PythonEcuador/PythonEcuador.github.io/issues>
(siempre asegúrate que alguien más no esté haciendo ya la tarea, así no gastamos esfuerzos).

También puedes ayudar revisando pull requests <https://github.com/PythonEcuador/PythonEcuador.github.io/pulls>
(la opinión de todos en bienvenida, pero siempre haciéndolo con respeto).

_**No sé programar o no me siento mucha confianza para empezar**_:
No todas las tareas involucran código,
simples correcciones ortográficas también aportan al proyecto.
Y si no te atreves a hacer la corrección por ti misma/o,
puedes [crear un issue](https://github.com/PythonEcuador/PythonEcuador.github.io/issues/new) indicando el problema

## Ejecutar el proyecto localmente

Si tienes dudas y/o problemas mientras sigues los pasos,
no dudes en preguntar en [nuestro canal de Telegram](https://t.me/pythonecuador).

### Python

Este proyecto usa Python 3, así que asegúrate de tenerlo instalado en tu sistema.
Puedes descargarlo desde <https://www.python.org/downloads/>.
Para verificar que tienes Python 3 en tu sistema ejecuta el siguiente comando en una terminal
(ventana de comandos).

```bash
python --version
 Python 3.6.5
```

Si la salida del comando es diferente, no te preocupes, sólo debes asegurarte que el primer número sea un `3`.
En caso que la salida haya sido algo como `2.7.14`, intenta con el comando `python3 --version`.

En caso que ambos comandos te den un error o no sea la versión adecuada,
asegúrate que Python esté en tun `PATH` o instala la versión adecuada.

En los pasos siguientes usaremos el comando `python`,
si el resultado de los pasos anteriores tuviste éxito haciéndolo con `python3`, debes usar ese comando.

### Obteniendo el proyecto

El proyecto está bajo el sistema de control de versiones git y alojado en GitHub,
puedes descargar git desde <https://git-scm.com/download>.

Haz un fork del proyecto desde GitHub (presionando el botón `Fork` en la parte superior).

Ejecuta el siguiente comando en una terminal (ventana de comandos)
para obtener el código. Donde `{tu-usuario}` es tu usuario de GitHub.

```bash
git clone https://github.com/{tu-usuario}/PythonEcuador.github.io.git
```

Entra al directorio que contiene el código fuente con

```bash
cd PythonEcuador.github.io
```

### Ejecutando el proyecto

El sitio está construido usando [Nikola](https://getnikola.com),
(no es necesario que sepas usarlo o que te leas toda la documentación para empezar a colaborar en el proyecto).

Antes de instalar Nikola, es recomendable que crees un entorno virtual para Python
(este paso debes hacerlo sólo una vez).

```bash
python -m venv venv
```

Ahora necesitamos activar el entorno virtual
(este paso debes hacerlo cada vez que abras un nuevo terminal/ventana de comandos)

```bash
# Para sistemas Linux y Mac
source venv/bin/activate
# Para sistemas Windows
venv\Scripts\activate
```

Ahora ya podemos instalar Nikola y otras dependencias

```bash
pip install -r requirements.txt
```

Finalmente, para ejecutar el sitio con Nikola

``` bash
nikola build
nikola serve
```

Si abres un navegador e ingresas a <http://127.0.0.1:8000/> podrás ver el sitio.

## Realizando cambios en el proyecto

Una vez que tengas un [issue](https://github.com/PythonEcuador/PythonEcuador.github.io/issues) con cual trabajar.
Crea una nueva rama con un nombre relacionado al issue que estás resolviendo.
`arregla-issue-13` es el nombre de la rama usada en este ejemplo.

```bash
git checkout -b arregla-issue-13
```

Haz los cambios que sean pertinentes para arreglar el issue.
Puedes ver los cambios en tu navegador mientras editas los archivos con el siguiente comando

```bash
nikola auto
```

Trata de hacer un commit para cada bloque de cambios relacionados que hagas

```
git add archivo-editado.rst
git commit -m "Arreglada falta ortográfica"
```

Una vez que hayas hechos todos los cambios necesarios, súbelos a tu fork

```
git push -u origin
```

Dirígete a la página del proyecto <https://github.com/PythonEcuador/PythonEcuador.github.io>
y verás un mensaje sugiriéndote hacer un pull request (PR).
En la descripción del PR describe brevemente los cambios que hiciste.
Espera a que un miembro de la comunidad revise tu PR,
si son necesarios más cambios, los puedes hacer en la misma rama
y repetir el proceso de agregar más commits y subiendo tus cambios con `git push`,
tus cambios serán actualizados en el PR que ya abriste inicialmente.
Si no hay más cambios y tu PR es aprobada, sólo debes esperar a que un miembro de la comunidad
haga un merge.