# -*- coding: utf-8 -*-


import pytest

from Fixture.Application import Application
from Model.Text_prod import Text_prod
from Model.Names_for_login import Name_log



@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy )
    return fixture
