Instructions to generate documentation with Sphinx
--------------------------------------------------

One-time setup
~~~~~~~~~~~~~~

- Install `sphinx <http://www.sphinx-doc.org/en/master/usage/installation.html>`_.
- Create a ``docs/`` directory in your project's directory.
- In a terminal, go to the ``docs/`` directory and run ``sphinx-quickstart`` to generate a ``conf.py`` and ``index.rst``, make sure you:

  - say yes to ``separate source and build directories``
  - keep the source file suffix as ``.rst``
  - say yes to autodoc: ``automatically insert docstrings from modules``
  - say yes to doctest

- Now you can generate html by running ``make html`` to check the build succeeded.
- To create a run configuration for this in PyCharm, add a new run configuration from ``Python Docs > Sphinx Task``, set the directory that contains ``conf.py`` as input (probably ``docs/source/``, and select the directory containing generated html files (probably ``docs/build/html``) as output.        
- Uncomment the following lines in ``docs/source/conf.py`` (probably lines 15-17):

  .. code-block::

     import os
     import sys
     sys.path.insert(0, os.path.abspath('.'))


  and change the last line to:

  .. code-block::

     sys.path.insert(0, os.path.abspath('../..'))

- Add each package to the table of contents, the toctree in ``index.rst``. In this example that would be the ``noodles`` and the ``spaghetti`` packages (subpackages will be automatically included):

  .. code-block::

     .. toctree::
        :maxdepth: 2

        noodles
        spaghetti
        
- Make sure each package and subpackage you want to have in the documentation contains a ``__init__.py`` file, including the ``src`` directory if you have it.        

Every time after changing docs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- **After changing/adding files/packages:** Run in a terminal in your project's top-level directory ``sphinx-apidoc -M -T -E -f -o docs/source .`` to generate a ``.rst`` file for each package. You can find what each option does in the `<apidoc documentation>`_. Do this every time you change something in your code/docstrings.
- **After changing documentation in the code:** Run the run configuration or ``make html`` to create the html.


For publishing the documentation on GitHub Pages, see for example https://daler.github.io/sphinxdoc-test/includeme.html#set-up-separate-docs-repository.
