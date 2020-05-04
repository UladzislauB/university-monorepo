import database
import DES

__server = '11'
__tgs = database.tgs_id


def SS_server(info):
    auth_encr = info['auth']
    tgs_encr = info['tgs']

    key_tgs_ss = database.keys[(__server, __tgs)]
    tgs = DES.decrypt(tgs_encr, key_tgs_ss)
    tgs = eval(tgs)
    key_c_ss = tgs['key']
    auth = DES.decrypt(auth_encr, key_c_ss)
    auth = eval(auth)

    if auth['c'] != tgs['c']:
        raise ValueError('Clients not equal')
    if auth['time'] - tgs['time'] > tgs['period']:
        raise ValueError('Period is not valid')

    response = auth['time'] + 1

    return DES.encrypt(str(response), key_c_ss)
