.. title: Mini tutorial de reStructuredText
.. slug: rst
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. template: pagina.tmpl

Esta guía es una breve introducción a los conceptos y la sintaxis de reStructuredText (reST).

reStructuredText es un lenguaje de marcado de texto, que es legible y simple de usar, pero lo suficientemente potente para un uso no trivial.
Es útil para la documentación de programas en línea (como las cadenas de documentación de Python),
para crear rápidamente páginas web simples y para documentos independientes.

.. note::
   Para seguir este tutorial te puedes ayudar de alguna herramienta para editar y previsualizar el resultado de la sintaxis RST. Recomendamos este `sitio <https://livesphinx.herokuapp.com/>`_ pero puedes usar la aplicación o sitio que mas te guste.

.. contents:: Contenidos
   :depth: 2

===================
Formato Básico
===================

Párrafo
-------

El párrafo es el bloque más básico en un documento reST.
Los párrafos son simplemente trozos de texto separados por una o más líneas en blanco.
Al igual que en Python, la sangría es significativa en reST,
por lo que todas las líneas del mismo párrafo deben alinearse a la izquierda con el mismo nivel de sangría.

+---------------------------------+----------------------------+
| Texto Plano                     | Resultado                  |
+=================================+============================+
|                                 |                            |
| ``Este es un párrafo.``         | Este es un párrafo.        |
|                                 |                            |
| ``Los párrafos se alinean al``  | Los párrafos se alinean al |         
| ``borde izquierdo y``           | borde izquierdo y          |
| ``normalmente están separados`` | normalmente están separados|
| ``por líneas en blanco.``       | por líneas en blanco.      |
+---------------------------------+----------------------------+


Formato de texto en línea
-------------------------

El formato de texto en línea permite que las palabras y frases dentro del texto tengan estilos de caracteres (como cursiva y negrita) y funcionalidad (como hipervínculos).

+--------------------------------------------+------------------------------------------+
| Texto Plano                                | Resultado                                |
+============================================+==========================================+
|                                            |                                          |
| | ``*itálica*``                            | | *itálica*                              |
| | ``**negrilla**``                         | | **negrilla**                           |         
| | ```link <https://pythonecuador.org>`__`` | | `link <https://pythonecuador.org>`__   |
| | ``normalmente están separados``          | | normalmente están separados            |
| | ``por líneas en blanco.``                | | por líneas en blanco.                  |
+--------------------------------------------+------------------------------------------+


===================
Comentarios
===================

Un comentario es una línea que no la vez en la previsualización pero si dentro del código o texto rst.

La sintaxis para agregar un comentario en rst. ``.. Esto es un comentario``. 

Como puedes ver agrega 2 puntos seguidos adelante de la línea que quieres comentar.

.. Esto es un comentario

========================
Mantener saltos de línea
========================

Normalmente en rst cuando das un salto de línea (enter) a mitad de la misma, este salto o nueva línea es ignorado.
En el caso de que quieras mantener los saltos de línea debes usar el prefijo **``|``** pipe, al inicio de cada nueva línea.

Por ejemplo para lograr esto:

| En esta línea saltaré
| a esta otra línea
| y a esta, manteniendo las nuevas líneas.

Usaremos la siguiente sintaxis::

    | En esta línea saltaré
    | a esta otra línea
    | y a esta, manteniendo las nuevas líneas.


===================
Texto Preformateado
===================

Es posible mostrar bloques de texto preformateados, Para esto se debe poner el signo dos puntos **(:)** 2 veces al final para obtener algo como esto::

        Cualquier sangría o tabulación es parte del bloque preformateado.
    Incluso 
 
    los
    saltos
    de línea     y      espacios.

Ahora la sintaxis usada para obtener el bloque preformateado anterior es la siguiente::


    Esta es la línea para iniciar un bloque preformateado, y al final agregamos doble 2 puntos::

            Cualquier sangría o tabulación es parte del bloque preformateado.
        Incluso
        saltos
        de línea       y       espacios.


===============
Links o enlaces
===============

Algo también interesante es poder incluir enlaces o links dentro de tu texto, y hay varias formas en que puedes hacerlo, por ejemplo:

- Puedes incluir un enlace personalizado como este `->Google <https://www.google.com>`_ en cualquier parte de tu texto::

   Sintaxis  de link personalizado `->Google <https://www.google.com>`_

  No olvides el guión bajo **(_)** al final.

- En caso de las direcciones webs no personalizadas como esta https://github.com se mostraran tal cual el formato o largo del URL::

   Sintaxis de link no personalizado  https://github.com

- Si quieres definir un link a la página de Wikipedia_, pero especificando el url por separado::

    Línea donde aparece el link_ definido por separado.

    .. _link: https://url-link/defino/por/separadp

.. _Wikipedia: https://es.wikipedia.org/wiki/Wikipedia:Portada

  Como puedes ver en la sintaxis, a la palabra link, se le agrega un guión bajo **(_)** al final ``link_`` para indicar que se definirá el url por separado.
  Luego en otro línea antepones el guión bajo **(_)** al incio de la plabra usada, en este caso ``_link`` para igualar o asigna el url a donde nos direcciona el enlace.

- Rst nos dá la facilidad de crear **enlaces internos** hacia el un documento. Para hacer esto podemos basarnos en el nombre de los encabezados que estén dentro de un archivo o documento, como por ejemplo este enlace `Formato Básico`_ me posiciona al inicio de este documento donde se explica el formato básico::

    Sintaxis para enlace a la sección de un documento: `Título del Encabezado a enlazar`_ 


===================
Listas
===================

Las listas son fáciles e intuitivas, incluso podemos tener listas anidadas, a continuación puedes ver los 2 tipos de listas que hay:


Listas desordenadas
-------------------

Puedes usar esta sintaxis:

.. code-block:: rst

    - Elemento 1
    - Elemento 2
        * Elemento 3
            + Elemento 4

**Resultado:**

- Elemento 1
- Elemento 2
    * Elemento 3
        + Elemento 4


Lista ordenada
---------------

Puedes obtener una lista ordenada o numerada con esta sintaxis:

.. code-block:: rst

    1. Elemento padre 1
        1.1 Elemento hijo de 1
            1.1.1 Elemento nieto de 1
    2. Elemento Padre 2
        2.1 Hijo de elemento 2
    3. Elemento 3

**Resultado:**

1. Elemento 1
    1.1 Elemento hijo de 1
        1.1.1 Elemento nieto de 1
2. Elemento 2
    2.1 Hijo de elemento 2
3. Elemento 3


========================
Títulos o encabezados
========================

Los encabezados se crean subrayando el texto del encabezado con un caracter o puntuación, este subrayado debe ser al menos tan largo como el texto.

.. code-block:: rst

    ==================
    Este es un título
    ==================


    Otro título
    ===========


Normalmente puedes subrayar un título, sección o encabezado con cualquier caracter o puntuación, debido a que no hay niveles de encabezados asignados a caracteres en específico, 
ya que esto se determina más por la estructura de los mismos encabezados.
 

Para para ayudarnos podemos seguir  la `Guía de estilo de documentación de Python <https://devguide.python.org/documenting/#style-guide>`_ que 
sigue esta convención para los títulos de encabezados.

- Subrayar con **``#``**, para encabezado de partes.
- Subrayar con **``*``**, para encabezado de capítulos.
- Subrayar con **``=``**, para encabezado de secciones (Título 1). 
- Subrayar con **``-``**, para encabezado de subsecciones (Título 2).
- Subrayar con **``^``**, para encabezado de sub-subsecciones (Título 3).
- subrayar con **``"``**, para los párrafos.

Aquí la sintaxis de ejemplo:

.. code-block:: rst

    #####################
    Título del documento 
    #####################

    Título de un capítulo
    *********************

    Título de una sección (Titulo 1)
    ================================

    Título de una subsección (Titulo 2)
    -----------------------------------

    Título de una sub-subsección (Titulo 3)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    Soy un párrafo
    """"""""""""""


Como ves no es necesario que subrayes los caracteres en la parte inferior y superior del encabezado, esto puede servir más para organización al editar el archivo.


**Resultado:** Imagen de captura del resultado

..image:: images/guias/rst/rst_encabezados.png


===================
Bloques de código
===================

Hay tres formas de agregar bloques de código con rst los cuales son equivalentes o dan el mismo resultado: ``code::``, ``sourcecode::``, y ``code-block::``.

En los bloques de código puedes agregar y mostrar código de cualquier lenguaje soportado, a continuación la sintaxis de ejemplo::

   .. code:: python

      import os
      print('Hellow World!')
      print(help(os))      


   .. sourcecode:: python

      import os
      print('Hellow World!')
      print(help(os))


   .. code-block:: python

       import os
       print('Hellow World!')
       print(help(os))

**Resultado:**

.. code:: python

    import os
    print('Hellow World!')
    print(help(os))

.. sourcecode::
    
    import os
    print('Hellow World!')
    print(help(os))

.. code-block:: python
    
    import os
    print('Hellow World!')
    print(help(os))


==============
Imágenes
==============

Puedes añadir imágenes y preformatear su tamaño o la posición al mostrarse, usando la siguiente sintaxis:::

    .. image:: screenshots/archivo-imagen.png
        :height: 100
        :width: 200
        :alt: alternate text


Además puedes agregar una imagen en línea con el texto usando la directiva |customsub|::

    Línea donde agregaremos imagen usando |customsub|

    .. |customsub| image:: screenshots/image1.png
              :alt: (imagen en lína con texto


.. |customsub| image:: screenshots/image1.png
              :alt: (imagen en lína con texto)


==========
Tablas
==========

Las tablas simples son fáciles de elaborar, pero tienen limitaciones. Por ejemplo podemos llegar a esto:

========== ========== 
Columna 1  Columna 2
========== ==========
Elemento1  Elemento1
Elemento2  Elemento2
Elemento3  Elemento3 
========== ==========


Escribiendo esta sintaxis::

    ========== ========== 
    Columna 1  Columna 2
    ========== ==========
    Elemento1  Elemento1
    Elemento2  Elemento2
    Elemento3  Elemento3 
    ========== ==========

En el caso de tablas más elaboradas, es necesario que nosotros mismos dibujemos la cuadrícula de las celdas, por ejemplo:

+-------------+-----------+------------------+
| Continente  | País      | Capital          |
+=============+===========+==================+
| America     | Ecuador   | Quito            |
+-------------+-----------+------------------+
| África      | Sudáfrica | Ciudad del Cabo  |
+-------------+-----------+------------------+
| Europa      | España    | Madrid           |
+-------------+-----------+------------------+
| Asia        | Japón     | Tokio            |
+-------------+-----------+------------------+
| ...         | ...       | ...              |
+-------------+-----------+------------------+

La obtenemos escribiendo la siguiente sintaxys::

    +-------------+-----------+-----------------+
    | Continente  | País      | Capital         |
    +=============+===========+=================+
    | America     | Ecuador   | Quito           |
    +-------------+-----------+-----------------+
    | África      | Sudáfrica | Ciudad del Cabo |
    +-------------+-----------+-----------------+
    | Europa      | España    | Madrid          |
    +-------------+-----------+-----------------+
    | Asia        | Japón     | Tokio           |
    +-------------+-----------+-----------------+
    | ...         | ...       | ...             |
    +-------------+-----------+-----------------+


O puedes elaborar incluso alguna donde una celda ocupe 2 filas o dos columnas, por ejemplo::

    +------------------------+------------+-----------+------------+
    | Fila cabecera,         | Celda doble columna    | Cabecera 3 |
    | columna 1              +------------+-----------+------------+ 
    | (cabeceras opcionales) | Cabecera 4 | Cabecera 5| Cabecera 6 |
    +========================+============+===========+============+
    | body row 1, column 1   | column 2   | column 3  | column 4   |
    +------------------------+------------+-----------+------------+
    | body row 2             | ...        | celda     |            |
    +------------------------+------------+ doble     +------------+
    | body row 2             | ...        | fila      |            |
    +------------------------+------------+-----------+------------+
    | body row 2             | ...        | ...       |            |
    +------------------------+------------+-----------+------------+

**Resultado:**

+------------------------+------------+-----------+------------+
| Fila cabecera,         | Celda doble columna    | Cabecera 3 |
| columna 1              +------------+-----------+------------+ 
| (cabeceras opcionales) | Cabecera 4 | Cabecera 5| Cabecera 6 |
+========================+============+===========+============+
| body row 1, column 1   | column 2   | column 3  | column 4   |
+------------------------+------------+-----------+------------+
| body row 2             | ...        | celda     |            |
+------------------------+------------+ doble     +------------+
| body row 2             | ...        | fila      |            |
+------------------------+------------+-----------+------------+
| body row 2             | ...        | ...       |            |
+------------------------+------------+-----------+------------+