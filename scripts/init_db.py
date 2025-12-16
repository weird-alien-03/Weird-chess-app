
from app.repo import connect, create_schema

conn = connect("tournament.db")
create_schema(conn)
print("DB initialized OK")
conn.close()
