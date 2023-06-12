# Tool to insert Mockaroo or any other sql generator file into DB.
1. Create env files in /env
    a. database.ini
        
        [mysql]
        host=hostname
        user=username
        database=dbname
        port=portname

    b. source.ini

        [mockaroo]
        url=url
        key=api key
        count=num of rows to generate
2. Run main.py