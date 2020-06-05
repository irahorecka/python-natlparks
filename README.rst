python-natlparks
================

A simple API wrapper for `US National Park Services <https://www.nps.gov/index.htm>`__.

License: `MIT <https://en.wikipedia.org/wiki/MIT_License>`__.

Getting an API key
------------------
You must have an API key with the National Park Services to use this library.
Register for your free API key `here <https://www.nps.gov/subjects/developer/get-started.htm>`__.

API examples
------------
Let's get started by instantiating a NatlParks object with your API key.

.. code:: python

    from natlparks import NatlParks
    parks = NatlParks(your_api_key)


Now, you can browse various API endpoints.

Activities: Activities are the primary categories of activities in which to participate in national parks.

.. code:: python

    parks.activities()  # default parameters: limit=50, start=1, q="", id=""
    parks.activities(limit=10, start=1, q="historical")
