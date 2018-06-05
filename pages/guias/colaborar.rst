.. title: Colaborar
.. slug: colaborar
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. template: pagina.tmpl

Recién estamos empezando, así que **hay mucho por hacer**.

  No sé programar o no tengo idea por dónde empezar

No todas las tareas involucran código,
correcciones ortográficas también aportan al proyecto.
Y si no te atreves a hacer la corrección por ti misma/o,
puedes al menos :ref:`reportar el problema <reportando-errores-bugs>`.
A continuación hemos redactado una guía para que puedas iniciar.

.. contents:: Contenidos
   :depth: 2

Si tienes dudas y/o problemas mientras sigues los pasos,
no dudes en preguntar en `nuestro canal de Telegram <https://t.me/pythonecuador>`_.

Ejecutar el proyecto localmente
-------------------------------

Python
######

Este proyecto usa Python 3, puedes descargarlo desde https://www.python.org/downloads/.
Para verificar que tienes Python 3 en tu sistema ejecuta el siguiente comando en una terminal
(ventana de comandos):

.. code:: console

   $ python --version
   Python 3.6.5

Si la salida del comando es diferente, no te preocupes, sólo debes asegurarte que el primer número sea un ``3``.
En caso que la salida haya sido algo como ``2.7.14``, intenta con el comando ``python3 --version``.

En caso que ambos comandos te den un error o no sea la versión adecuada,
asegúrate que Python esté en tu ``PATH`` o instala la versión adecuada.

.. note::

   En los pasos siguientes usaremos el comando ``python``,
   si el resultado de los pasos anteriores tuviste éxito haciéndolo con ``python3``,
   debes usar ese comando.

Obteniendo el proyecto
######################

El proyecto está bajo el sistema de control de versiones Git y alojado en GitHub,
puedes descargar Git desde https://git-scm.com/download.

Debes tener una cuenta en `GitHub <https://github.com/>`_, inicia sesión,
dirígete al `proyecto de Python Ecuador <https://github.com/PythonEcuador/PythonEcuador.github.io>`_
y presiona el botón ``Fork`` para hacer un fork del proyecto en tu cuenta.

.. image:: /images/guias/colaborar/fork.png
   :align: center

Ejecuta el siguiente comando en una terminal para obtener el código.
Donde ``{tu-usuario}`` es tu usuario de GitHub.

.. code:: bash

   git clone https://github.com/{tu-usuario}/PythonEcuador.github.io.git

Entra al directorio que contiene el código fuente con

.. code:: bash
   
   cd PythonEcuador.github.io

.. note::

   El desarrollo se lleva a cabo sobre la rama ``src``.
   Por defecto tu repositorio debe estar en esta rama.
   Si tienes dudas ejecuta:

   .. code:: bash
      
      git checkout src

Ejecutando el proyecto
######################

El sitio está construido usando `Nikola <https://getnikola.com>`_
(no es necesario que sepas usarlo para empezar a colaborar en el proyecto).

Crea un entorno virtual para instalar las dependencias de Python
(este paso debes hacerlo sólo una vez):

.. code:: bash

   python -m venv venv

Con ese comando acabamos de crear un entorno virtual llamado ``venv``.
Puedes leer más sobre los entornos virtuales de Python en https://docs.python.org/3/library/venv.html.

Ahora necesitamos activar el entorno virtual
(este paso debes hacerlo cada vez que abras una nuevo terminal):

.. code:: bash

   # Para sistemas Linux y Mac
   source venv/bin/activate

   # Para sistemas Windows
   venv\Scripts\activate

Ahora ya podemos instalar Nikola y otras dependencias:

.. code:: bash

   pip install -r requirements.txt

Finalmente, para ejecutar el sitio con Nikola

.. code:: bash
   
   nikola build
   nikola serve

Si abres tu navegador e ingresas a http://127.0.0.1:8000/ podrás ver el sitio.

Reportando errores (bugs)
-------------------------

GitHub usa ``issues`` para dar seguimiento a tareas y reportar bugs.
Si encuentras un error o tienes una idea para mejorar el sitio,
`crea un nuevo issue <https://github.com/PythonEcuador/PythonEcuador.github.io/issues/new>`_
describiendo el bug/mejora.

.. note::

  Asegúrate que el bug no haya sido reportado antes o que ya exista una idea similar.
  Busca en los `issues ya creados <https://github.com/PythonEcuador/PythonEcuador.github.io/issues>`_.

Buscando tareas
---------------

Puedes mirar en los `issues abiertos <https://github.com/PythonEcuador/PythonEcuador.github.io/issues>`_
para buscar tareas por hacer.
Los issues contienen etiquetas (`labels <https://github.com/PythonEcuador/PythonEcuador.github.io/labels>`_)
para clasificarlos por complejidad y/o tipo.

`Good First Issue`_
  Tareas de complejidad fácil que te ayudarán a familiarizarte con el proyecto.
`Bug`_, `Enhancement`_
  Si ya resolviste suficientes tareas fáciles y quieres pasar al siguiente nivel.
`Design`_
  Si lo tuyo es el diseño gráfico o web.
`duplicate`_
  Indica issues similares o pull requests
`help wanted`_
  Indica que uno de los administradores busca ayuda en un issue o pull request
`invalid`_
  Indica  que el issue o pull request no es relevante
`question`_
  Indica que issues similares o pull request necesitan más información
`ready`_
  Indica que el issue esta listo
`wip`_
    Indica que el issue está en progreso (Work in Progress)
`wontfix`_
    Indica que el trabajo no va a continuar en un issue o pull request

.. _Good First Issue: https://github.com/PythonEcuador/PythonEcuador.github.io/labels/good%20first%20issue
.. _Bug: https://github.com/PythonEcuador/PythonEcuador.github.io/labels/bug
.. _Enhancement: https://github.com/PythonEcuador/PythonEcuador.github.io/labels/enhancement
.. _Design: https://github.com/PythonEcuador/PythonEcuador.github.io/labels/design
.. _duplicate: https://github.com/PythonEcuador/PythonEcuador.github.io/labels/duplicate
.. _help wanted: https://github.com/PythonEcuador/PythonEcuador.github.io/labels/help%20wanted
.. _invalid: https://github.com/PythonEcuador/PythonEcuador.github.io/labels/invalid
.. _question: https://github.com/PythonEcuador/PythonEcuador.github.io/labels/question
.. _ready: https://github.com/PythonEcuador/PythonEcuador.github.io/labels/ready
.. _wip: https://github.com/PythonEcuador/PythonEcuador.github.io/labels/wip
.. _wontfix: https://github.com/PythonEcuador/PythonEcuador.github.io/labels/wontfix

También puedes ayudar `revisando pull requests <https://github.com/PythonEcuador/PythonEcuador.github.io/pulls>`_.

.. note::

  Siempre asegúrate que alguien más ya no esté haciendo la tarea, así no gastamos esfuerzos.


Realizando cambios
------------------

Una vez que tengas un issue con cual trabajar.
Crea una nueva rama con un nombre relacionado al issue que estás resolviendo.
`arregla-issue-13` es el nombre de la rama usada en este ejemplo.

.. code:: bash

   git checkout -b arregla-issue-13

Haz los cambios que sean pertinentes para resolver el issue.
Puedes ver los cambios en tu navegador mientras editas los archivos con el siguiente comando

.. code:: bash

   nikola auto

Trata de hacer un commit por cada bloque de cambios relacionados que hagas

.. code:: bash

   git add archivo-editado.rst
   git commit -m "Arreglada falta ortográfica"

Una vez que hayas hechos todos los cambios necesarios, súbelos a tu fork

.. code:: bash

   git push -u origin arregla-issue-13

Dirígete a la `página del proyecto <https://github.com/PythonEcuador/PythonEcuador.github.io>`_
y verás un mensaje sugiriéndote hacer un pull request (PR).
En la descripción del PR describe brevemente los cambios que hiciste.

Espera a que un miembro de la comunidad revise tu PR,
si son necesarios más cambios, los puedes hacer en la misma rama
y repetir el proceso de agregar más commits.

.. code:: bash

   git add archivo-editado.rst
   git commit -m "Más cambios"

Una vez que ya los tengas listos, vuelve a subirlos

.. code:: bash
   
   git push

.. note::

   Tus cambios serán actualizados en el PR que ya abriste inicialmente.
   Así que no es necesario que vuelvas a abrir otro.

Si no son necesarios más cambios y tu PR es aprobada,
sólo debes esperar a que un miembro de la comunidad haga un merge.

Estructura del proyecto
#######################

files/
  Archivos generales del sitio
pages/
  Aquí están todas las páginas del sitio
posts/
  Posts del sitio
themes/custom/
  Tema personalizado del sitio
themes/custom/assets/
  JavaScript, CSS, etc
themes/custom/templates/
  Aquí están los templates; son archivos parecidos a html reutilizables
conf.py
  En este archivo están las configuraciones del sitio

Editar una página incompleta
############################

Si te topaste con una página con el título *¡Esta sección necesita de tu ayuda!*,
para empezar a editarla debes localizar la página (se encuentran en el directorio ``pages/``)
cada archivo corresponde a la URL de la página, por ejemplo si la página es ``www.python.ec/eventos``
el archivo a editar se encontrará en ``pages/eventos.rst``.
Los archivos están escritos en `reStructuredText <http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_.

  ¡Pero ahí no está toda la página que vi en el navegador!

Ya vamos a esa parte.

Como podrás notar, al principio del archivo, se encuentran metadatos. Como:

- ``title``: El título de la página
- ``slug``: El path del URL
- ``template``: El template a ser usado para la página

Existen otros, pero esos son los más relevantes, sobre todo el de template.
Por defecto estará en ``ayuda.tmpl``, tu primer paso será cambiarlo por ``pagina.tmpl``.
Estos templates contienen el contenido base de la página (se encuentran en ``themes/custom/templates/``).
Y los archivos ``.rst`` sólo contienen el texto principal.

Ahora sólo necesitas editar el archivo ``.rst`` ¡y listo!

Crear una nueva página
######################

Pronto

Creando una nueva sección
#########################

Pronto

Mi segundo Pull Request
#######################

¿Ya por el segundo? ¡Felicitaciones!
Antes de enviar tu segundo pull request,
debes hacer un par de pasos para igualar tu fork con los últimos cambios del repositorio.

.. note::

   Asegúrate de repetir este proceso antes de tomar una nueva tarea.

Primero debemos cambiarnos nuevamente a la rama principal (``src``).


.. code:: bash

   git checkout src

Asegúrate que no tengas cambios residuales de tu anterior PR
antes de proceder con los siguientes pasos
(puedes usar ``git status`` para comprobarlo).

Necesitaremos hacerle saber a git del repo principal con el siguiente comando.

.. code:: bash
   
   git remote add upstream https://github.com/PythonEcuador/PythonEcuador.github.io.git

Ahora ya podemos bajarnos los últimos cambios del repo principal.

.. code:: bash
   
   git pull upstream src

Y los subimos a nuestro fork

.. code:: bash

   git push origin src

Ahora si, puedes seguir los pasos indicados :ref:`arriba <realizando-cambios>`
para continuar con tu próximo pull request.

FAQ
---

¿Qué es un sitio estático?
##########################

Es un sitio con contenido que nunca cambia,
a diferencia de un sitio dinámico dónde el contenido cambia con interacciones de los usuarios.

¿Por qué no se hizo un sitio dinámico usando un framework como Django?
######################################################################

Un sitio estático no requiere de un servidor ni de mucho esfuerzo para desplegar.
Puede ser alojado en GitHub Pages sin ningún costo.
Es totalmente escalable y configurable.

¿Por qué se usó Nikola?
#######################

Se hizo una pequeña votación antes de empezar con el desarrollo del sitio en
`#2 <https://github.com/PythonEcuador/PythonEcuador.github.io/issues/2>`__.
