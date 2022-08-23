import configparser

config = configparser.RawConfigParser()
config.read("./Configuration/config.config.ini")

class ReadConfig:
    @staticmethod
    def getUrl():
        url = config.get('common-info', 'baseURL')
        return  url
    
    @staticmethod
    def getUserName():
        password = config.get('common-info', 'userName')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common-info', 'password')
        return password