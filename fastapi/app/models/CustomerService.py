import pandas as pd
import psycopg2


class CustomerService():

    def __init__(self):
        self.con = psycopg2.connect(
            host="192.168.0.103",
            # host="localhost",
            port="5432",
            database='FlaskToFastapi',
            user='postgres',
            password='L+10221022',
        )

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
