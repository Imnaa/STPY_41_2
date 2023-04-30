import DB.DBConnect
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

class SqlQueryes():

    def __init__(self, db):
        self.__db = db

    def InnerAllTables(self) -> pd.DataFrame():  # sourcery skip: extract-duplicate-method
        df = pd.DataFrame()
        
        query = """
            select *
            from boarding_passes as bp
        """
        sql_r = pd.read_sql(query, self.__db.connection)
        df_boarding_passes = pd.DataFrame(sql_r)
        #print(df_boarding_passes)

        query = """
            select *
            from ticket_flights as tf 
        """
        sql_r = pd.read_sql(query, self.__db.connection)
        df_ticket_flights = pd.DataFrame(sql_r)
        #print(df_ticket_flights)

        df = pd.merge(df_boarding_passes, df_ticket_flights, how='outer', left_on=['ticket_no','flight_id'], right_on=['ticket_no','flight_id'])
        df_boarding_passes = None
        df_ticket_flights = None

        query = """
            select *
            from flights as f 
        """
        sql_r = pd.read_sql(query, self.__db.connection)
        df_flights = pd.DataFrame(sql_r)
        #print(df_flights)
        df = pd.merge(df, df_flights, how='outer', left_on=['flight_id'], right_on=['flight_id'])
        df_flights = None
        df= df.drop(columns=['flight_id'], axis=1)

        query = """
            select *
            from aircrafts as ac 
        """
        sql_r = pd.read_sql(query, self.__db.connection)
        df_aircrafts = pd.DataFrame(sql_r)
        #print(df_aircrafts)
        df = pd.merge(df, df_aircrafts, how='outer', left_on=['aircraft_code'], right_on=['aircraft_code'])
        df_aircrafts = None
        df= df.drop(columns=['aircraft_code', 'range'], axis=1)

        query = """
            select *
            from airports as ap
        """
        sql_r = pd.read_sql(query, self.__db.connection)
        df_airports = pd.DataFrame(sql_r)
        #print(df_airports)
        df = pd.merge(df, df_airports, how='outer', left_on=['departure_airport'], right_on=['airport_code'])
        df = pd.merge(df, df_airports, how='outer', left_on=['arrival_airport'], right_on=['airport_code'])
        df_airports = None
        # df= df.drop(columns=[
        #     'longitude_x', 'latitude_x', 'timezone_x','longitude_y', 'latitude_y', 'timezone_y',
        #     'airport_code_x', 'airport_code_y'], axis=1)
        df= df.drop(columns=[
            'timezone_x', 'timezone_y',
            'airport_code_x', 'airport_code_y'], axis=1)

        # query = """
        #     select *
        #     from seats as tf 
        # """
        # sql_r = pd.read_sql(query, self.__db.connection)
        # df_seats = pd.DataFrame(sql_r)
        #print(df_seats)

        query = """
            select *
            from tickets as tf 
        """
        sql_r = pd.read_sql(query, self.__db.connection)
        df_tickets = pd.DataFrame(sql_r)
        #print(df_tickets)
        df = pd.merge(df, df_tickets, how='outer', left_on=['ticket_no'], right_on=['ticket_no'])
        df_tickets = None
        df= df.drop(columns=[
            'passenger_id', 'contact_data'], axis=1)

        query = """
            select *
            from bookings as tf 
        """
        sql_r = pd.read_sql(query, self.__db.connection)
        df_bookings = pd.DataFrame(sql_r)
        #print(df_bookings)
        df = pd.merge(df, df_bookings, how='outer', left_on=['book_ref'], right_on=['book_ref'])
        df_bookings = None


        return df