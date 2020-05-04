import database
import datetime
import DES
from AS_server import AS_server
from TGS_server import TGS_server
from SS_server import SS_server

__client = '10'
__client_key = database.clients[__client]
__target = '11'


# AS_server
def authorization():
    authorization_decr = AS_server(__client)
    if not authorization_decr:
        raise ValueError('No such user in database')

    print('\tAS_server encrypted response:')
    print(authorization_decr)

    authorization = DES.decrypt(authorization_decr, __client_key)

    print('\n\tAS_server decrypted response:')
    print(authorization)

    return eval(authorization)


# TGS_server
def tgs_server(auth):
    info = {
        'tgt': auth['tgt'],
        'auth': DES.encrypt(str({'c': __client, 'time': datetime.datetime.now().timestamp()}), auth['key']),
        'id': __target
    }

    print('\n\tRequest to TGS_server:')
    print(info)

    res_encr = TGS_server(info)

    print('\n\tTGS_server encrypted response:')
    print(res_encr)

    res = DES.decrypt(res_encr, auth['key'])

    print('\n\tTGS_server decrypted response:')
    print(res)

    return eval(res)


# SS_server
def ss_server(tgs_ans):
    time = datetime.datetime.now().timestamp()
    info = {
        'tgs': tgs_ans['tgs'],
        'auth': DES.encrypt(str({'c': __client, 'time': time}), tgs_ans['key'])
    }

    print('\n\tRequest to SS_server:')
    print(info)

    res_encr = SS_server(info)

    print('\n\tSS_server encrypted response:')
    print(res_encr)
    res = eval(DES.decrypt(res_encr, tgs_ans['key']))

    print('\n\tSS_server decrypted response:')
    print(res)

    if abs(res - time - 1) > 1e-6:
        raise ValueError("Not connected")

    print('\n\nOK. Connected')


def main():
    auth = authorization()
    tgs_ans = tgs_server(auth)
    print(tgs_ans)
    ss_server(tgs_ans)


if __name__ == '__main__':
    main()
