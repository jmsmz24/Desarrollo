import psycopg2

conn = psycopg2.connect('dbname=test')
cur = conn.cursor()

insert_query = "INSERT INTO people (name, company) VALUES ('alberto','telefonica')"
print(insert_query)
cur.execute(insert_query)
conn.commit()
