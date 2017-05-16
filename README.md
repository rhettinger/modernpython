Modern Python: Big ideas, Little Code
=====================================

This code is offered as an accompaniment to a Python Video course
by Raymond Hettinger.

See [Modern Python: Big Ideas, Little Code][1].

Raymond runs an international Python training and consulting
company and is available for basic, intermediate, and advanced
python training.

[1]: http://www.informit.com/store/modern-python-livelessons-big-ideas-and-little-code-9780134743417


Getting Setup
-------------

1) Install Python 3.6.1 or later from https://www.python.org

2) Setup and activate a virtual environment:

```bash
    $ python3.6 -m venv modernpython
    $ source modernpython/bin/activate
```

3) Install the packages used in the examples:

```bash
    (modernpython) $ pip install pyflakes
    (modernpython) $ pip install bottle
    (modernpython) $ pip install pytest
    (modernpython) $ pip install hypothesis
    (modernpython) $ pip install mypy
```

Resampling
----------

This code demonstrates simulations, resampling, bootstrapping,
hypothesis testing, and estimating confidence intervals.


Machine Learning
----------------

The `kmeans.py` file implements k-means from scratch.  The
`congress_data` directory has CSV files with the voting histories
of senators in the 114th U.S. Congress.  The `congress.py` file
demonstrates ETL (extract-transfrom-load) and unsupervised
machine learning (k-means) to analyze the voting clusters.


Publisher Subscriber
--------------------

This code implements a simple publisher-subscriber notification
service.  The `pubsub.py` implements the data model and core
services.  The `session.py` loads sample data.  The `webapp.py`
file runs a webserver for the application.  The `views` directory
has the Bottle templates and the `static` directory has the
static resources (icons and photos).

To start the service, run:

```bash
    (modernpython) $ python webapp.py
```

Then point your browser to `http://localhost:8080/`

The login information is in the `session.py` file.


Testing
-------

The `quadratic.py` file is a module with a simple function to
demonstrate various approaches to testing included in
`test_quadratic.py`.


Validation
----------

The `pricing_tool.py` file is used to demonstrate the descriptor
based data validation tools in `validators.py`

