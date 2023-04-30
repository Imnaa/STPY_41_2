class DBKeys:
    def __init__(self):
        self.__Key_DBUser="postgres"
        self.__Key_DBPassword="111"
        self.__Key_DBHost="127.0.0.1"
        self.__Key_DBPort="5432"
        self.__Key_DBDatabase="avia"
        self.__Key_DBOptions="-c search_path=dbo,bookings"

    def getDBUser(self):
        return self.__Key_DBUser
    def getDBPassword(self):
        return self.__Key_DBPassword
    def getDBHost(self):
        return self.__Key_DBHost
    def getDBPort(self):
        return self.__Key_DBPort
    def getDBDatabase(self):
        return self.__Key_DBDatabase
    def getDBOptions(self):
        return self.__Key_DBOptions