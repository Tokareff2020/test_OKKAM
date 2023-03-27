import psycopg2

from db.config_parser import DBNAME, USERNAME, HOST, PASSWORD


async def get_respondent_from_str(audience: str = ''):
    conn = psycopg2.connect(f"dbname={DBNAME} user={USERNAME} host={HOST} password={PASSWORD}")
    with conn:
        with conn.cursor() as cur:
            cur.execute(f'SELECT respondent, AVG(Weight) from respondent_table'
                        f' where {audience} group by respondent')
            result = cur.fetchall()
    return result
