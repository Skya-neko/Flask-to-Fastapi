import pandas as pd
import psycopg2
con = psycopg2.connect(
    host="localhost",
    port="5432",
    database='FlaskToFastapi',
    user='postgres',
    password='L+10221022',
)



class customer():
    def __init__(self, con):
        self.con = con

    def select_info(self):
        query = """
        SELECT * FROM customer
        """
        df = pd.read_sql(query, con)
        return df.to_json(orient="split")

