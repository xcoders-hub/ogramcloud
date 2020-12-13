import configparser as ConfigParser

# Configs parameters
configParser = ConfigParser.RawConfigParser()   
configFilePath = r'config.txt'
configParser.read(configFilePath)

# Filling parameters
TOKEN = '1225137582:AAGpFuy-wN75GSuZxs2N3DGCoyzBeoRsnbU'
UPLOAD_FOLDER = configParser.get('ogram-config', 'UPLOAD_FOLDER')
