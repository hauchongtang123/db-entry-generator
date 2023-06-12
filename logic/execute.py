from connection.connect import connect_cursor

def execute_repeat(query="", times=1) -> None:
    conn, cur = connect_cursor()
    # Process the script
    query_list = query.split(";\n")
    # Execute SQL script
    print("Executing queries...")
    p_key_id = 1
    for idx in range(times):
        if idx % 10 == 0:
            print(f'Query at row {idx}:{idx+10}')
        for q in query_list:
            if q == "":
                continue
            q = q.replace("{'id':'id'}", str(p_key_id))
            cur.execute(q+";")
            p_key_id += 1
    conn.commit()
    print("Commiting...")
    cur.close()
    print("Done!")
    conn.close()
    print("Connection Closed")