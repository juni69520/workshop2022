from pandas import array
from dotenv import load_dotenv
import os
import psycopg2
import datetime
import time

class insertData:
    def insert(tableau=array, tableName=''):
        load_dotenv()
        try:
            conn = psycopg2.connect(
                        host=os.getenv("host"),
                        port=os.getenv("port"),
                        database=os.getenv("database"),
                        user=os.getenv("user"),
                        password=os.getenv("password"),
                    )
            sql = "INSERT INTO "+tableName+" (angry, disgust, fear, happy, sad, surprise, neutral, user_id, created_at) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);"
            createdAt = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            cur = conn.cursor()
            cur.execute(sql, (tableau['angry'],tableau['disgust'],tableau['fear'],tableau['happy'],tableau['sad'],tableau['surprise'],tableau['neutral'],tableau['user_id'], createdAt))
            conn.commit()
            conn.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
                print('Database connection closed.')