import configparser as ConfigParser

# Configs parameters configParser.get('your-config', 'path1')
configParser = ConfigParser.RawConfigParser()
configFilePath = r'config.txt'
configParser.read(configFilePath)

# Filling parameters
SPLASH_SCRAP_URL = configParser.get('falla-config', 'SPLASH_SCRAP_URL')
