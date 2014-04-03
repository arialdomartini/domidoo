from domidooweb import DBSession
from domidooweb.models.tag import Tag
from domidooweb.models.tag_repository import TagRepository
from domidooweb.tests.integration_tests import IntegrationTests

__author__ = 'arialdomartini'


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
        actual.name.should.be.equal('bar')


    def test_all_tags_can_be_retrieved(self):

        DBSession.add(Tag(name = 'name1'))
        DBSession.add(Tag(name = 'name2'))
        DBSession.add(Tag(name = 'name3'))
        DBSession.add(Tag(name = 'name4'))

        sut = TagRepository()

        actual = sut.get_all()

        names = [tag.name for tag in actual]
        names.should.contain('name1')
        names.should.contain('name2')
        names.should.contain('name3')
        names.should.contain('name4')