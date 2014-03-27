import unittest
import transaction
import os
from pyramid import testing

from domidooweb.models import *
from domidooweb.views import *
from domidooweb.admin_views import *
from integration_tests import IntegrationTests 

from domidooweb.domain import TagRepository

class PlaceRepositoryTests(IntegrationTests):

    def test_a_tag_can_be_retrieved_by_by_name(self):
        tag=Tag('foobar')
        DBSession.add(tag)

        sut = TagRepository()

        actual = sut.get_or_create_by_name('foobar')

        assert actual.name == 'foobar'
        assert actual == tag


    def test_if_no_tag_is_found_get_by_name_creates_it(self):
        sut = TagRepository()
        actual = sut.get_or_create_by_name('bar')

        assert actual != None
        assert actual.name == 'bar'
