# -*- coding: utf-8 -*-

from Model.Text_prod import Text_prod
from Model.Names_for_login import Name_log


def test_delete_prod(app):
    app.session_.login (Name_log(emaillogin="dmitriy115@i.ua", password="00000" ) )
    if app.Prodhelper.count () == 0:
        app.Prodhelper.add_new_prod(Text_prod(firstname="Квартира", price="10000", quantity="1", description="Супер", file="\kv1.jpg"))
    app.Prodhelper.delete_prod()
