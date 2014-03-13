import unittest
import transaction
import os
from pyramid import testing

from domidooweb.models import *
from domidooweb.views import *
from domidooweb.admin_views import *
from integration_tests import IntegrationTests 

from domidooweb.domain import PlaceRepository

dburl = 'sqlite://'
class PlaceRepositoryTests(IntegrationTests):

    def test_a_place_can_be_retrieved_from_the_db(self):
        place=Place('name', 'city', 'image')
        DBSession.add(place)

        sut = PlaceRepository()

        actual = sut.get_first()

        assert actual.name == 'name'
        assert actual.city == 'city'
        assert actual.image == 'image'

    def test_a_place_can_be_retrieved_from_the_db_by_by_id(self):
        place=Place('name', 'city', 'image')
        DBSession.add(place)
        placeid = place.id

        sut = PlaceRepository()

        actual = sut.get(placeid)

        assert actual.name == 'name'
        assert actual.city == 'city'
        assert actual.image == 'image'

    def test_all_placec_can_be_retrieved(self):

        DBSession.add(Place('name1', 'city', 'image'))
        DBSession.add(Place('name2', 'city', 'image'))
        DBSession.add(Place('name3', 'city', 'image'))
        DBSession.add(Place('name4', 'city2', 'image'))

        sut = PlaceRepository()

        actual = sut.get_all()

        names = [p.name for p in actual]
        assert 'name1' in names
        assert 'name2' in names
        assert 'name3' in names
        assert 'name4' in names

