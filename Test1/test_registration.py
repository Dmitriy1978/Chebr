# -*- coding: utf-8 -*-

from Model.Names_for_login import Name_reg, Name_adm, Name_conf, Name_log


def test_authorization(app):
     app.registrationHelp.registration(Name_reg( firstname="dtest", lastname="TesterD", username="dddd", emaillogin="dmitriy117@i.ua",
                      phone="1111111111", password="11111" ) )
     app.registrationHelp.confirm_login(Name_conf( emaillogin="dmitriy117@i.ua", passwordf="dmitriy115" ) )
     app.session.login(Name_log( emaillogin="dmitriy117@i.ua", password="11111" ) )
     #app.session.logout_any()
     app.registrationHelp.delete_user(Name_adm(logina="root", passworda="1stEnter"))





