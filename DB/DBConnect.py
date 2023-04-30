import psycopg2

class DBConnect:

    def __init__(self, user, password, host, port, database, options):
        self.__user = user
        self.__password = password
        self.__host = host
        self.__port = port
        self.__database = database
        self.__options = options

    def Connect(self):
        try:
            self.connection = psycopg2.connect(user=self.__user,
                                        password=self.__password,
                                        host=self.__host,
                                        port=self.__port,
                                        database=self.__database,
                                        options=self.__options)


            self.cursor = self.connection.cursor()
            # print("Информация о сервере PostgreSQL")
            # print(self.connection.get_dsn_parameters(), "\n")
            self.cursor.execute("SELECT version();")
            record = self.cursor.fetchone()
            print("Вы подключены к -", record, "\n")

        except (Exception) as error:
            print("Ошибка при работе с PostgreSQL", error)
            
    def Disconnect(self):
        try:
            if self.connection:
                self.cursor.close()
                self.connection.close()
                print("Соединение с PostgreSQL закрыто")
        except (Exception) as error:
            print("Ошибка при работе с PostgreSQL", error)