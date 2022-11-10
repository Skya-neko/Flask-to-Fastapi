import pandas as pd
import psycopg2
con = psycopg2.connect(
    host="192.168.0.103",
    port="5432",
    database='FlaskToFastapi',
    user='postgres',
    password='L+10221022',
)

class CustomerService():
    _instance = None

    def __init__(self, con):
        self.con = con
        if self._instance is None:
            self._instance = self

    @staticmethod
    def getInstance():
        if CustomerService._instance is None:
           CustomerService(con)
        return CustomerService._instance

    def getCustomers(self):
        query = """
            SELECT * FROM customer
        """
        df = pd.read_sql(query, self.con)
        return df.to_json(orient="split")

    def getCustomerById(self, id):
        query = f"""
                    SELECT * FROM customer where id = {id}
                """
        df = pd.read_sql(query, self.con)
        return df.to_json(orient="split")
