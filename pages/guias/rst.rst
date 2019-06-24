.. title: Mini tutorial de reStructuredText
.. slug: rst
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. template: pagina.tmpl

Esta guía es una breve introducción a los conceptos y la sintaxis de reStructuredText (reST).

restructuredText es legible y simple, pero lo suficientemente potente para un uso no trivial.
Es útil para la documentación de programas en línea (como las cadenas de documentación de Python),
para crear rápidamente páginas web simples y para documentos independientes.

.. contents:: Contenidos
   :depth: 2

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
