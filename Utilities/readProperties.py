import configparser

config = configparser.RawConfigParser()
config.read('.//configuration//config.ini')

class ReadProperties:
    @staticmethod
    def getApplicationUrl():
        url = config.get('common info', 'baseUrl')
        return url

    @staticmethod
    def getApplicationRegisterUrl():
        url = config.get('common info', 'registerUrl')
        return url
    @staticmethod
    def getUserEmail():
        email = config.get('common info', 'userEmail')
        return email

    @staticmethod
    def getUserPassword():
        password = config.get('common info', 'userPassword')
        return password