import pymysql
from ..vars import var


async def mysqlq(query, save=False):
    con = pymysql.connect(
        host=var.DB_HOST, 
        user=var.DB_USER, 
        password=var.DB_PASSWOORD, 
        database=var.DB_NAME
    )

    cursor = con.cursor()
    cursor.execute(query)

    if save:
        con.commit()
        return True
    
    return cursor.fetchall()