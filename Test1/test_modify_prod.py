from Model.Text_prod import Modify_prod
from Model.Names_for_login import Name_log


def test_modify_prod(app):

    app.session_.login (Name_log(emaillogin="dmitriy115@i.ua", password="00000" ))
    app.session_.insure_login (firstname = "test", lastname = "tester")
    app.Prodhelper.modify_prod(Modify_prod( firstname="Квартира new", price="20000", quantity="2", file="\kv2.jpg" ) )
    #app.session.Logout_any ()