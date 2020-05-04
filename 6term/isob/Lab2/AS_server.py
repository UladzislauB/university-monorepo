import database
import datetime
import DES


def AS_server(c_id: str):
    if c_id not in database.clients:
        return {}

    k_c = database.clients[c_id]
    tgs_id = database.tgs_id
    k_c_tgc = database.keys[(c_id, tgs_id)]

    tgt = {
        'c': c_id,
        'tgs': tgs_id,
        'time': datetime.datetime.now().timestamp(),
        'period': 1000,
        'key': k_c_tgc
    }

    res = {
        'tgt': DES.encrypt(str(tgt), database.K_as_tgs),
        'key': k_c_tgc
    }

    return DES.encrypt(str(res), k_c)
