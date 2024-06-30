from database.DB_connect import DBConnect
from model.locali import Locale


class DAO():
    def __init__(self):
        pass
    @staticmethod
    def getCitta():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct b.city as citta
from business b
order by b.city"""

        cursor.execute(query)

        for row in cursor:
            result.append(row["citta"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getNodi(citta, anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct b.*, avg(r.stars) as mediaRecensioni
from business b, reviews r 
where b.business_id=r.business_id 
and b.city=%s and year(r.review_date )=%s
 group by b.business_id"""

        cursor.execute(query,(citta,anno,))

        for row in cursor:
            result.append(Locale(**row))

        cursor.close()
        conn.close()
        return result

