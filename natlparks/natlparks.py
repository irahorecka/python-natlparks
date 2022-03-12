from functools import wraps
import inspect

import requests

from natlparks.exceptions import HTTPError


class BaseAPI(object):
    """Base API wrapper for individual national park http requests."""

    base_url = "https://developer.nps.gov/api/v1"
    api_param = {"api_key": "your_api_key_here"}

    def __init__(self, api_key):
        self.api_param["api_key"] = api_key

    def get_json(self):
        try:
            response = requests.get(self.url, params=self.api_param)
        except requests.exceptions.ConnectionError as e:
            raise HTTPError(e) from e

        return response.json()


def api_method(method):
    """Decorator for generating appropriate url endpoints."""
    default_kwargs = dict(
        zip(inspect.getargspec(method).args[1:], inspect.getargspec(method).defaults)
    )  # get default kwargs

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        method(self, *args, **kwargs)
        kwargs = {**default_kwargs, **kwargs}
        if method.__name__ != "__call__":
            self.url = f"{self.base_url}/{self.api}/{method.__name__}"
        else:
            self.url = f"{self.base_url}/{self.api}"

        if kwargs:
            extension = "&".join(f"{key}={value}" for key, value in kwargs.items() if value)
            self.url = f"{self.url}?{extension}"

        return self.get_json()

    return wrapper


class Activities(BaseAPI):
    """API for national park activities. Activities are the
    primary categories of activities in which to participate
    in national parks."""

    api = "activities"

    @api_method
    def __call__(self, limit=50, start=1, q="", id=""):
        pass

    @api_method
    def parks(self, limit=50, start=1, q="", id=""):
        """API for national parks activities parks information."""
        pass


class Alerts(BaseAPI):
    """API for national park alerts. Alerts communicate information
    about hazardous, potentially hazardous, or changing conditions
    that may affect a visit to a national park. Alert data includes
    the type of alert, title, description, and optional link to
    additional information."""

    api = "alerts"

    @api_method
    def __call__(self, limit=50, start=1, q="", parkCode="", stateCode=""):
        pass


class Amenities(BaseAPI):
    """API for national park amenities."""

    api = "amenities"

    @api_method
    def __call__(self, limit=50, start=1, q="", id=""):
        pass

    @api_method
    def parksplaces(self, limit=50, start=1, q="", id="", parkCode=""):
        """API for national park parks places."""
        pass

    @api_method
    def parksvisitorcenters(self, limit=50, start=1, q="", id="", parkCode=""):
        """API for national park visitor center amenities."""
        pass


class Articles(BaseAPI):
    """API for national park articles. Articles are shared content
    assets that are tagged so they can appear in a variety of places
    on NPS.gov. Data includes a title, image, short description of
    the content, and link to more information about the asset."""

    api = "articles"

    @api_method
    def __call__(self, limit=50, start=1, q="", parkCode="", stateCode=""):
        pass


class Campgrounds(BaseAPI):
    """API for national park campgrounds. Campground data includes
    location, contact, operating hours, site amenities, fee, and
    accessibility information for campgrounds in national parks At
    least one representative photo of each campground is available
    Some parks have multiple campgrounds of a variety of types
    (eg, developed or primitive); others have none."""

    api = "campgrounds"

    @api_method
    def __call__(self, limit=50, start=1, q="", parkCode="", stateCode=""):
        pass


class Events(BaseAPI):
    """API for national park events. Event data includes information
    about the date, time, fee, and description of events taking place
    in national parks."""

    api = "events"

    @api_method
    def __call__(
        self,
        limit=50,
        start=1,
        pageSize=10,
        pageNumber=1,
        expandRecurring=False,
        q="",
        id="",
        parkCode="",
        dateStart="",
        dateEnd="",
    ):
        pass


class LessonPlans(BaseAPI):
    """API for national park lesson plans. Lesson plans are standards-based
    resources about national parks for teacher to use in their classrooms
    Lesson plan data includes objectives, grade level, subject, duration,
    and standards information."""

    api = "lessonplans"

    @api_method
    def __call__(self, limit=50, start=1, q="", parkCode="", stateCode=""):
        pass


class NewsReleases(BaseAPI):
    """API for national park news releases. News release data includes a
    title, abstract, and link to national park news releases, as well as an
    optional image."""

    api = "newsreleases"

    @api_method
    def __call__(self, limit=50, start=1, q="", parkCode="", stateCode=""):
        pass


class Parks(BaseAPI):
    """API for national parks. Park basics data includes location, contact,
    operating hours, and entrance fee/pass information for each national
    park At least five photos of each park are also available."""

    api = "parks"

    @api_method
    def __call__(self, limit=50, start=1, q="", parkCode="", stateCode=""):
        pass


class People(BaseAPI):
    """API for national park people. People are shared content assets that
    are tagged so they can appear in a variety of places on NPS.gov. Data
    includes a title, image, short description of the content, and link to
    more information about the asset."""

    api = "people"

    @api_method
    def __call__(self, limit=50, start=1, q="", parkCode="", stateCode=""):
        pass


class Places(BaseAPI):
    """API for national park places. Places are shared content assets that
    are tagged so they can appear in a variety of places on NPS.gov. Data
    includes a title, image, short description of the content, and link to
    more information about the asset."""

    api = "places"

    @api_method
    def __call__(self, limit=50, start=1, q="", parkCode="", stateCode=""):
        pass


class Topics(BaseAPI):
    """API for national park topics. Topics are the primary categories of
    topics interpreted by national parks."""

    api = "topics"

    @api_method
    def __call__(self, limit=50, start=1, q="", id=""):
        pass

    @api_method
    def parks(self, limit=50, start=1, q="", id=""):
        """API for national park topic parks information."""
        pass


class VisitorCenters(BaseAPI):
    """API for national park visitor centers. Visitor center data includes
    location, contact, and operating hours information for visitor centers
    and other visitor contact facilities in national parks At least one
    visitor center is listed for each park; some parks with multiple visitor
    centers may include information about more than one."""

    api = "visitorcenters"

    @api_method
    def __call__(self, limit=50, start=1, q="", parkCode="", stateCode=""):
        pass


class NatlParks(object):
    """Python wrapper for the national park API."""

    activities = None
    alerts = None
    amenities = None
    articles = None
    campgrounds = None
    events = None
    lesson_plans = None
    news_releases = None
    parks = None
    people = None
    places = None
    topics = None
    visitor_centers = None

    def __init__(self, api_key):
        """Instantiate individual API request classes with api_key."""
        args = (api_key,)
        self.activities = Activities(*args)
        self.alerts = Alerts(*args)
        self.amenities = Amenities(*args)
        self.articles = Articles(*args)
        self.campgrounds = Campgrounds(*args)
        self.events = Events(*args)
        self.lesson_plans = LessonPlans(*args)
        self.news_releases = NewsReleases(*args)
        self.parks = Parks(*args)
        self.people = People(*args)
        self.places = Places(*args)
        self.topics = Topics(*args)
        self.visitor_centers = VisitorCenters(*args)
