import psycopg2


create_table = 'CREATE TABLE films_planet_bridge2( film_id integer, planet_id integer);'
insert_data =  'insert into films_planet_bridge2(film_id, planet_id) select raw_starwars_films."index" , raw_starwars_planets."index" from raw_starwars_films join raw_starwars_planets on position(raw_starwars_films.url in raw_starwars_planets.films) > 0;'
query = f"{create_table}{insert_data}"

conn = psycopg2.connect(database='postgres', user='postgres', password='maytheforcebewithyou', port="5432")

with conn:
    with conn.cursor() as curs:
        curs.execute(query)

conn.commit()
conn.close()
