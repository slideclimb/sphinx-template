Setup sphinx, or add it to an existing Python project
-----------------------------------------------------

- Install `sphinx <http://www.sphinx-doc.org/en/master/usage/installation.html>`_.
- Run ``sphinx-quickstart`` to generate a ``conf.py`` and ``index.rst``, make sure you:
   - say yes to ``separate source and build directories``
   - say yes to ``automatically insert docstrings from modules``
- Now you can generate html by running ``make html``.
- To create a run configuration for this in PyCharm, add a new run configuration from ``Python Docs > Sphinx Task``, set the directory that contains ``conf.py`` as input, and the ``_build/html`` as output.
- Uncomment the following lines in the ``conf.py`` (probably lines 15-17):

  .. code-block::

     import os
     import sys
     sys.path.insert(0, os.path.abspath('.'))


  and change the last line to:

  .. code-block::

     sys.path.insert(0, os.path.abspath('../..'))


- Run ``sphinx-apidoc -M -T -E -f -o docs/source .`` to generate a ``.rst`` file for each package. You can find what each option does in the `<apidoc documentation>`_. Do this every time you change something in your code/docstrings.
- Add each package to the table of contents, the toctree in ``index.rst``. In this example that would be the ``noodles`` and the ``spaghetti`` packages:

  .. code-block::

     .. toctree::
        :maxdepth: 2

        noodles
        spaghetti
