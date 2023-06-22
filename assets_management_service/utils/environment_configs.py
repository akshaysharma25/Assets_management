import configparser

configs = configparser.ConfigParser()
configs.read('config.ini')
configs.sections()


class EnvironmentConfigs:
    db = configs['DATABASE']['db']
    dbName = configs['DATABASE']['dbName']
    dbHost = configs['DATABASE']['dbHost']
    dbPort = configs['DATABASE']['dbPort']
    dbUser = configs['DATABASE']['dbUser']
    dbPassword = configs['DATABASE']['dbPassword']

    issuer_url = configs['IDP']['issuer_url']