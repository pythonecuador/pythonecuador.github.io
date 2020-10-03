.. title: Deploy
.. slug: deploy
.. type: text
.. template: pagina.tmpl

.. warning::

   Esta guía es para pesonas con permisos de escritura sobre el repositorio.
   Usarla con responsabilidad.

.. note::

   Los deploys ahora se realizan de manera automática, cada vez que se realiza un merge
   de un commit a la rama principal (src).

En esta guía aprenderemos a desplegar el sitio a producción usando `Nikola <https://getnikola.com>`__.

.. contents:: Contenidos
   :depth: 2

Preparando tu entorno local
###########################

Siguiendo los pasos de `la guía de contribución <link://filename/pages/guias/colaborar.rst>`__
deberías tener tu instancia local funcionando.

Comprobando la funcionalidad del sitio
######################################

Antes de desplegar el sitio, asegúrate que:

- El sitio está funcional (``make serve``)
- Todas las pruebas están pasando en `travis <https://travis-ci.org/PythonEcuador/PythonEcuador.github.io>`__
- No hay errores o warnings importantes al compilar el sitio (``make serve``)

Desplegar
#########

Tenemos un archivo make para facilitar el deploy, úsalo. Asegúrate que:

#. Estés en la rama adecuada (``git checkout src``)
#. No tengas cambios locales (``git status`` debe estar limpio)
#. Tengas los últimos cambios del repositorio (``git pull origin src``)
#. El sitio está funcional

Para desplegar el sitio, usamos el comando ``make deploy``.
Debes ver un mensaje de éxito en caso que todo haya salido bien.

Puedes chequear la rama master_ para verificar que los archivos compilados se encuentran subidos.
Los cambios podrán ser vistos en https://python.ec en aproximadamente 5 minutos.

.. _master: https://github.com/PythonEcuador/PythonEcuador.github.io/tree/master

Dominio
#######

El dominio usado actualmente es python.ec,
si necesitas acceso a las configuraciones del dominio,
pregunta en el `grupo de Telegram`_.

.. _grupo de Telegram: https://t.me/pythonecuador

Errores comunes
###############

¿Encontraste un error al hacer un deploy? ¡Documenta la solución aquí!
