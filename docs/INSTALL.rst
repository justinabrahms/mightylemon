Installation
============

Installing ``virtualenv``
-------------------------

``virtualenv`` is a way to isolate a python environment so it doesn't
affect your system python. It is similar to ``zc.buildout``, but
operates on the shell level rather than the file level. Using
``virtualenv`` requires no alteration to your python files to use it.

To install ``virtualenv``, use ``easy_install``:

::

  sudo easy_install virtualenv

Once its intalled, we'll need to create a virtualenv. You can name it
whatever you like, but I tend to call mine ``env``.

::

  virtualenv env
  source env/bin/activate

The first command creates a virtual enviornment where all of our
packages will be installed. The second command activates the
``virtualenv``. You'll know its active if you have an ``(env)`` in
your prompt.

NOTE: You'll need to ensure you have ``(env)`` in your prompt before
working with this project, else you won't have access to the things
you install.

Installing ``pip``
------------------

Once your ``virtualenv`` has been activated, install ``pip``.

::

  easy_install pip

This gives you a more full-featured way to install python
packages. The main benefit for this project is you can install from
git, svn, and mercurial repositories.


Installing ``mightylemon``
--------------------------

::

  git clone git://justinlilly.com/pub/mightylemon.git mightylemon
  cd mightylemon
  pip install -r requirements.txt
  cp local_settings.py.template local_settings.py
  python manage.py syncdb
  python manage.py runserver

So let's take this line by line.

In the first portion, we check out the source into a folder called
``mightylemon``, then enter that directory. Then, using ``pip``, we
install all of the necessary packages for the project. These
dependencies are listed in the requirements file along with the
version number if relevant. We then copy a template of our
``local_settings`` file which will manage our database settings. These
are put into a separate file as they'll change from host to host. Once
that's done, we're ready to create the database and start up the
development server.
