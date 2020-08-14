import os
import pyAesCrypt

class LoginInfoTest:
    def test_get_store_values(store):
        # one way to get the value
        user = store.get('a_general_user')
        username = user['username']
        # or another
        username = store.get('a_general_user').get('username')
        # or even another
        password = store.get('a_general_user')['password']
        # or
        user_type = store['a_general_user']['usertype']
        # ...
        some_site.log_in(username, password, user_type)
