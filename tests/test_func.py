from myfirstpackage.lib import who_i_am

def test_type_str():
    assert type(who_i_am()) == str