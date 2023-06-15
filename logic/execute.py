from connection.connect import connect_cursor
from helpers.days import generate_random_days, generate_sql_datetime

def execute_repeat(query="", thousand_times=1) -> None:
    # guard clause
    if query == "":
        Exception("Query is empty!")
        return
    
    conn, cur = connect_cursor()
    # Process the script
    query_list = query.split(";\n")
    # Execute SQL script
    print("Executing queries...")
    p_key_id = 1
    for idx in range(thousand_times):
        if idx % 10 == 0:
            print(f'Query at index {idx}')
        for q in query_list:
            if q == "":
                continue
            q = q.replace("{'id':'id'}", str(p_key_id))
            whitelist = f"'{generate_random_days()}'"
            q = q.replace("{'promo_apply_days':'promo_apply_days'}", whitelist)
            q = q.replace("{'dt':'dt'}", f"'{generate_sql_datetime(p_key_id)}'")
            cur.execute(q+";")
            p_key_id += 1
    conn.commit()
    print("Commiting...")
    cur.close()
    print("Done!")
    conn.close()
    print("Connection Closed")