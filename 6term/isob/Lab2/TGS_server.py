import database
import DES
from datetime import datetime


def TGS_server(info: dict):
    tgt_encr = info['tgt']
    auth_encr = info['auth']
    service_id = info['id']

    tgt = DES.decrypt(tgt_encr, database.K_as_tgs)
    tgt = eval(tgt)
    k_c_tgs = tgt['key']

    auth = DES.decrypt(auth_encr, tgt['key'])
    auth = eval(auth)

    if auth['c'] != tgt['c']:
        raise ValueError('client id not equal')

    if auth['time'] - tgt['time'] > tgt['period']:
        raise ValueError('ticket is not valid')

    k_tgs_ss = database.keys[(service_id, database.tgs_id)]
    k_c_ss = database.keys[tuple(sorted((service_id, auth['c'])))]

    tgs = {
        'c': auth['c'],
        'ss': service_id,
        'time': datetime.now().timestamp(),
        'period': 1000,
        'key': k_c_ss
    }

    res = {
        'tgs': DES.encrypt(str(tgs), k_tgs_ss),
        'key': k_c_ss
    }

    return DES.encrypt(str(res), k_c_tgs)
