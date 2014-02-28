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

