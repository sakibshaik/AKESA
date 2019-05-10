import pytest

from nlp.module import ModuleClass, module_function


@pytest.fixture
def klass():
    return ModuleClass('bar')


def test_fixture(klass):
    assert klass._foo == 'bar'


def test_fubction():
    assert module_function() == 1
