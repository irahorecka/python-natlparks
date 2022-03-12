import os
from pathlib import Path
import sys
import unittest

os.chdir(Path(__file__).parent)
os.chdir("../natlparks")
sys.path.append(os.getcwd())  # required for relative file fetching - run in 'test' directory
from natlparks import NatlParks


class TestNatlParks(unittest.TestCase):
    limit = 40
    start = 4
    q = "yosemite"

    def setUp(self):
        API_Token = os.environ.get("NATL_PARK_API")
        self.natl_parks = NatlParks(API_Token)

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

    def test_visitor_centers(self):
        visitor_centers = self.natl_parks.visitor_centers()
        self.assertIsInstance(visitor_centers, dict)
        visitor_centers = self.natl_parks.visitor_centers(
            limit=self.limit, start=self.start, q=self.q
        )
        self.assertIsInstance(visitor_centers, dict)


if __name__ == "__main__":
    unittest.main()
