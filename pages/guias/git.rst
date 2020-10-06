.. title: Instalar Git
.. slug: git
.. type: text
.. template: pagina.tmpl

Instalar Git en Ubuntu/Debian
-----------------------------
Antes de instalar es recomendable ejecutar las actualizaciones de paquetes del sistema operativo, por ende abrimos una terminal y ejecutamos lo siguiente:

Para actualizar los repositorios.

.. code:: console

   $ sudo apt-get update

Para actualizar los paquetes en el sistema.

.. code:: console

   $ sudo apt-get upgrade

Luego procedemos a instalar git con el comando install.

.. code:: console

   $ sudo apt-get install git

Este comando instalará git y sus paquetes necesarios.

.. image:: /images/guias/git/git_install.png
   :align: center

|

Comprobamos que se haya instalado correctamente con:

.. code:: console

   $ sudo git --version
   git version 2.25.1

Instalar Git en Fedora
----------------------
Instalar mediante DNF (o Yum en versiones mas antiguas de Fedora)

.. code:: console

   $ sudo dnf install git
   o
   $ sudo yum install git

Comprobamos que se haya instalado correctamente con:

.. code:: console

   $ sudo git --version
   git version 2.25.1




