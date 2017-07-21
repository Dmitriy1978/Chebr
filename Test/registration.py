# -*- coding: utf-8 -*-


import pytest

from Fixture.Application import Application
from Model.Names_for_login import Name_reg, Name_adm, Name_conf, Name_log


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy )
    return fixture


def test_authorization(app):
     app.registration(Name_reg( firstname="dtest", lastname="TesterD", username="dddd", emaillogin="dmitriy117@i.ua",
                      phone="1111111111", password="11111" ) )
     app.confirm_login(Name_conf( emaillogin="dmitriy117@i.ua", passwordf="dmitriy115" ) )
     app.Login(Name_log( emaillogin="dmitriy117@i.ua", password="11111" ) )
     app.Logout_any ()
     app.delete_user(Name_adm(logina="root", passworda="1stEnter"))






