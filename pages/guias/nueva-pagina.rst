.. title: Nueva página
.. slug: nueva-página
.. tags:
.. category:
.. link:
.. description:
.. type: text
.. template: pagina.tmpl


Crear nueva página
-------------------


Para crear una nueva página ejecutamos los siguiente:

.. code:: console
  
  $ nikola new_page

Tu nueva página estará ubicada en: ``pages/nueva_pagina.rst`` en el encabezado de la página coloca ``templeate: pagina.tmpl`` para usar el mismo template que el resto de páginas.

Si necesitas que se encuentre en otra ubicación, por ejemplo dentro del la carpeta **guias**  ejecuta:

.. code:: console

  $ cd pages
  $ mv pagina.rst guias/



