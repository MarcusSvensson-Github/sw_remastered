import psycopg2

def create_intermediate_bridges(resources):
    root_table = resources[0]
    resources.remove(root_table)

    print('\nroot table', root_table,'\nRemaining resources to go through:', resources)

    for resource in resources:
        create_table = f'CREATE TABLE {root_table}_{resource}_bridge({root_table}_id integer, {resource}_id integer);'
        insert_data =  f'insert into {root_table}_{resource}_bridge({root_table}_id, {resource}_id) select raw_starwars_{root_table}."index" , raw_starwars_{resource}."index" from raw_starwars_{root_table} join raw_starwars_{resource} on position(raw_starwars_{root_table}.url in raw_starwars_{resource}.{root_table}) > 0;'
        query = f"{create_table}{insert_data}"

        conn = psycopg2.connect(database='postgres', user='postgres', password='maytheforcebewithyou', host="postgresdb", port="5432")

        with conn:
            with conn.cursor() as curs:
                curs.execute(query)

    conn.commit()
    conn.close()