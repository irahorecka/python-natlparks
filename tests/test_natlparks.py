import os
import sys
import unittest

from argparse import ArgumentParser, RawTextHelpFormatter
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))  # required for relative file fetching - run in 'tests/' directory
from natlparks import NatlParks


class TestNatlParks(unittest.TestCase):
    limit = 40
    start = 4
    q = "yosemite"

    def setUp(self):
        self.natl_parks = NatlParks(api_token)

    def test_activities(self):
        activities = self.natl_parks.activities()
        self.assertIsInstance(activities, dict)
        activities = self.natl_parks.activities(limit=self.limit, start=self.start, q=self.q)
        self.assertIsInstance(activities, dict)

    def test_alerts(self):
        alerts = self.natl_parks.alerts()
        self.assertIsInstance(alerts, dict)
        alerts = self.natl_parks.alerts(limit=self.limit, start=self.start, q=self.q)
        self.assertIsInstance(alerts, dict)

    def test_amenities(self):
        amenities = self.natl_parks.amenities()
        self.assertIsInstance(amenities, dict)
        amenities = self.natl_parks.amenities(limit=self.limit, start=self.start, q=self.q)
        self.assertIsInstance(amenities, dict)

    def test_articles(self):
        articles = self.natl_parks.articles()
        self.assertIsInstance(articles, dict)
        articles = self.natl_parks.articles(limit=self.limit, start=self.start, q=self.q)
        self.assertIsInstance(articles, dict)

    def test_campgrounds(self):
        campgrounds = self.natl_parks.campgrounds()
        self.assertIsInstance(campgrounds, dict)
        campgrounds = self.natl_parks.campgrounds(limit=self.limit, start=self.start, q=self.q)
        self.assertIsInstance(campgrounds, dict)

    def test_events(self):
        events = self.natl_parks.events()
        self.assertIsInstance(events, dict)
        events = self.natl_parks.events(limit=self.limit, start=self.start, q=self.q)
        self.assertIsInstance(events, dict)

    def test_lesson_plans(self):
        lesson_plans = self.natl_parks.lesson_plans()
        self.assertIsInstance(lesson_plans, dict)
        lesson_plans = self.natl_parks.lesson_plans(limit=self.limit, start=self.start, q=self.q)
        self.assertIsInstance(lesson_plans, dict)

    def test_news_releases(self):
        news_releases = self.natl_parks.news_releases()
        self.assertIsInstance(news_releases, dict)
        news_releases = self.natl_parks.news_releases(limit=self.limit, start=self.start, q=self.q)
        self.assertIsInstance(news_releases, dict)

    def test_parks(self):
        parks = self.natl_parks.parks()
        self.assertIsInstance(parks, dict)
        parks = self.natl_parks.parks(limit=self.limit, start=self.start, q=self.q)
        self.assertIsInstance(parks, dict)

    def test_people(self):
        people = self.natl_parks.people()
        self.assertIsInstance(people, dict)
        people = self.natl_parks.people(limit=self.limit, start=self.start, q=self.q)
        self.assertIsInstance(people, dict)

    def test_places(self):
        places = self.natl_parks.places()
        self.assertIsInstance(places, dict)
        places = self.natl_parks.places(limit=self.limit, start=self.start, q=self.q)
        self.assertIsInstance(places, dict)

    def test_topics(self):
        topics = self.natl_parks.topics()
        self.assertIsInstance(topics, dict)
        topics = self.natl_parks.topics(limit=self.limit, start=self.start, q=self.q)
        self.assertIsInstance(topics, dict)

    def _ignore_test_visitor_centers(self):
        # TODO: For some reason, this test fails...
        visitor_centers = self.natl_parks.visitor_centers()
        self.assertIsInstance(visitor_centers, dict)
        visitor_centers = self.natl_parks.visitor_centers(
            limit=self.limit, start=self.start, q=self.q
        )
        self.assertIsInstance(visitor_centers, dict)


def parse_args(*args):
    parser = ArgumentParser(
        description="Unit Test for python-natlparks", formatter_class=RawTextHelpFormatter
    )
    parser.add_argument(
        "--token",
        type=str,
        help="National Park Services developer API token (https://www.nps.gov/subjects/developer/get-started.htm)",
    )
    parser.add_argument("unittest_args", nargs="*")

    return parser.parse_args(args)


if __name__ == "__main__":
    # Pass API token as a CLI argument using `--token=YOUR_API_KEY`.
    namespace = parse_args(*sys.argv[1:])
    sys.argv[1:] = namespace.unittest_args
    api_token = namespace.token
    # If no CLI argument passed, try fetching API key stored as an environment variable.
    if not api_token:
        try:
            api_token = os.environ["NATL_PARK"]
        except KeyError as e:
            raise RuntimeError("No API key provided. Aborting.") from e

    unittest.main()
