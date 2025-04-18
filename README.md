# python-natlparks

<p align="center">
  <img src="https://www.nps.gov/articles/images/NPS-Transparent-Logo.png" width="20%"/>
</p>

<br>

[![pypiv](https://img.shields.io/pypi/v/python-natlparks.svg)](https://pypi.python.org/pypi/python-natlparks)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![tests](https://github.com/irahorecka/python-natlparks/workflows/tests/badge.svg)](https://github.com/irahorecka/python-natlparks/actions)
[![Licence](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/irahorecka/python-natlparks/main/LICENSE)

A simple API wrapper for [US National Park
Services](https://www.nps.gov/index.htm).

## Getting an API key

You must have an API key with the National Park Services to use this
library. Register for your free API key
[here](https://www.nps.gov/subjects/developer/get-started.htm).

## API documentation

Thorough National Park Service API documentation can be found
[here](https://www.nps.gov/subjects/developer/api-documentation.htm#/).

## Installation

    pip install python-natlparks

## API examples

Let\'s get started by instantiating a NatlParks object with your API
key.

``` python
from natlparks import NatlParks
parks = NatlParks(your_api_key)
```

Now, you can browse various API endpoints.

**Activities**: Activities are the primary categories of activities in
which to participate in national parks.

``` python
parks.activities()  # default parameters: limit=50, start=1, q="", id=""
parks.activities(limit=10, start=1, q="historical")
```

**Activities parks**: Returns activities parks information.

``` python
parks.activities.parks()  # default parameters: limit=50, start=1, q="", id=""
parks.activities.parks(limit=10, start=1, q="historical")
```

**Alerts**: Alerts communicate information about hazardous, potentially
hazardous, or changing conditions that may affect a visit to a national
park. Alert data includes the type of alert, title, description, and
optional link to additional information.

``` python
parks.alerts()  # default parameters: limit=50, start=1, q="", parkCode="", stateCode=""
parks.alerts(limit=10, start=1)
```

**Amenities**: Returns amenities information.

``` python
parks.amenities()  # default parameters: limit=50, start=1, q="", id=""
parks.amenities(limit=10, start=1)
```

**Amenities parks places**: TBD.

``` python
parks.amenities.parksplaces()  # default parameters: limit=50, start=1, q="", id="", parkCode=""
parks.amenities.parksplaces(limit=10, start=1)
```

**Amenities parks visitor centers**: Returns amenities parks visitor
centers information.

``` python
parks.amenities.parksvisitorcenters()  # default parameters: limit=50, start=1, q="", id="", parkCode=""
parks.amenities.parksvisitorcenters(limit=10, start=1)
```

**Articles**: Articles are shared content assets that are tagged so they
can appear in a variety of places on NPS.gov. Data includes a title,
image, short description of the content, and link to more information
about the asset.

``` python
parks.articles()  # default parameters: limit=50, start=1, q="", parkCode="", stateCode=""
parks.articles(limit=10, start=1)
```

**Campgrounds**: Campground data includes location, contact, operating
hours, site amenities, fee, and accessibility information for
campgrounds in national parks At least one representative photo of each
campground is available Some parks have multiple campgrounds of a
variety of types (eg, developed or primitive); others have none.

``` python
parks.campgrounds()  # default parameters: limit=50, start=1, q="", parkCode="", stateCode=""
parks.campgrounds(limit=10, start=1)
```

**Events**: Event data includes information about the date, time, fee,
and description of events taking place in national parks.

``` python
parks.events()  # default parameters: limit=50, start=1, pageSize=10, pageNumber=1, expandRecurring=False, q="", id="", parkCode="", dateStart="", dateEnd=""
parks.events(limit=10, start=1)
```

**Lesson plans**: Lesson plans are standards-based resources about
national parks for teacher to use in their classrooms. Lesson plan data
includes objectives, grade level, subject, duration, and standards
information.

``` python
parks.lesson_plans()  # default parameters: limit=50, start=1, q="", parkCode="", stateCode=""
parks.lesson_plans(limit=10, start=1)
```

**News releases**: News release data includes a title, abstract, and
link to national park news releases, as well as an optional image.

``` python
parks.news_releases()  # default parameters: limit=50, start=1, q="", parkCode="", stateCode=""
parks.news_releases(limit=10, start=1)
```

**Parks**: Park basics data includes location, contact, operating hours,
and entrance fee/pass information for each national park At least five
photos of each park are also available.

``` python
parks.parks()  # default parameters: limit=50, start=1, q="", parkCode="", stateCode=""
parks.parks(limit=10, start=1)
```

**People**: People are shared content assets that are tagged so they can
appear in a variety of places on NPS.gov. Data includes a title, image,
short description of the content, and link to more information about the
asset.

``` python
parks.people()  # default parameters: limit=50, start=1, q="", parkCode="", stateCode=""
parks.people(limit=10, start=1)
```

**Places**: Places are shared content assets that are tagged so they can
appear in a variety of places on NPS.gov. Data includes a title, image,
short description of the content, and link to more information about the
asset.

``` python
parks.places()  # default parameters: limit=50, start=1, q="", id=""
parks.places(limit=10, start=1)
```

**Topics**: Topics are the primary categories of topics interpreted by
national parks.

``` python
parks.topics()  # default parameters: limit=50, start=1, q="", id=""
parks.topics(limit=10, start=1)
```

**Topics parks**: Returns topics parks information.

``` python
parks.topics.parks()  # default parameters: limit=50, start=1, q="", id=""
parks.topics.parks(limit=10, start=1)
```

**Visitor centers**: Visitor center data includes location, contact, and
operating hours information for visitor centers and other visitor
contact facilities in national parks At least one visitor center is
listed for each park; some parks with multiple visitor centers may
include information about more than one.

``` python
parks.visitor_centers()  # default parameters: limit=50, start=1, q="", parkCode="", stateCode=""
parks.visitor_centers(limit=10, start=1)
```

## Contribute

-   [Issues
    Tracker](https://github.com/irahorecka/python-natlparks/issues)
-   [Source
    Code](https://github.com/irahorecka/python-natlparks/tree/master/python-natlparks)

## Support

If you are having issues or would like to propose a new feature, please
use the [issues
tracker](https://github.com/irahorecka/python-natlparks/issues).

## License

This project is licensed under the MIT license.
