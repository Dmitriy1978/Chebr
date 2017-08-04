# -*- coding: utf-8 -*-


import pytest

from Fixture.Application import Application
from Model.Text_prod import Text_prod
from Model.Names_for_login import Name_log

fixture = None

#@pytest.fixture(scope="session")
@pytest.fixture()
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.is_valid():
            fixture = Application ()
    return fixture

@pytest.fixture (scope="session", autouse = True)
def stop (request):
    def fin():
        fixture.session.ensure_Logout_any ()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

