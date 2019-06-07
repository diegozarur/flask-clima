import os

_basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfiguration(object):
    DEBUG = True
    TESTING = False

    API_TOKEN = '13c7e771771a118603fc868d9f6b43fd'
    API_HOST = 'http://apiadvisor.climatempo.com.br'
    API_HOST_CITY = 'http://apiadvisor.climatempo.com.br/api/v1/locale/city?name={}&token=' + API_TOKEN
    API_HOST_FORECAST = 'http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/{}/days/15?token=' + API_TOKEN
