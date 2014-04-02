import unittest
import transaction
import os
import sure
from pyramid import testing

from domidooweb.allmodels import *
from domidooweb.views import *
from domidooweb.admin_views import *
from integration_tests import IntegrationTests 

from domidooweb.domain import PlaceRepository

dburl = 'sqlite://'
class PlaceRepositoryTests(IntegrationTests):

    def test_a_place_can_be_retrieved_from_the_db(self):
        place=Place('name', 'city')
        DBSession.add(place)

        sut = PlaceRepository()

        actual = sut.get_first()

        actual.name.should.be.equal('name')
        actual.city.should.be.equal('city')


    def test_a_place_can_be_retrieved_from_the_db_by_by_id(self):
        place=Place('name', 'city')
        DBSession.add(place)
        placeid = place.id

        sut = PlaceRepository()

        actual = sut.get(placeid)

        actual.name.should.be.equal('name')
        actual.city.should.be.equal('city')


    def test_all_place_can_be_retrieved(self):

        DBSession.add(Place('name1', 'city'))
        DBSession.add(Place('name2', 'city'))
        DBSession.add(Place('name3', 'city'))
        DBSession.add(Place('name4', 'city2'))

        sut = PlaceRepository()

        actual = sut.get_all()

        names = [p.name for p in actual]
        names.should.contain('name1')
        names.should.contain('name2')
        names.should.contain('name3')
        names.should.contain('name4')

