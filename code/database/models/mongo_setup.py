import mongoengine
import ssl


def global_init(user=None, password=None, port=27017, server='localhost', use_ssl=True, db_name='school_scheduler'):
    if user or password:

        data = dict(
            username=user,
            password=password,
            host=server,
            port=port,
            authentication_source='admin',
            authentication_mechanism='SCRAM-SHA-1',
            ssl=use_ssl,
            ssl_cert_reqs=ssl.CERT_NONE)

        mongoengine.register_connection(alis='core', name=db_name, **data)
        data['password'] = 'admin'
        print(" --> Registering prod connection: {}".format(data))
    else:
        print(" --> Registering dev connection:")
        mongoengine.register_connection(alias='core', name=db_name)
