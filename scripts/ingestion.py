import requests
import pandas as pd
from sqlalchemy import create_engine
import psycopg2
import time
import json



def build_starwars_db(resources):
    """
    pipeline for starwars api
    """
    engine = create_engine('postgresql+psycopg2://postgres:maytheforcebewithyou@postgresdb/postgres')
    

    for resource in resources:
        build_table(resource, engine)



def build_table(resource, engine):
    
    url = f"https://swapi.dev/api/{resource}"
    table_name = f"raw_starwars_{resource}"

    print('fetching', url)
    response = requests.get(url)

    if response.status_code == 200:
        print('Building table', table_name)
        data = response.json()

        raw_data = data["results"]   #contain the api body of interest with films as list
        print(raw_data[0])

        next_page_url = data['next']
        while next_page_url:
            print('fetching', next_page_url, '\n')
            response = requests.get(next_page_url)
            data = response.json()
            next_page_url = data['next']
            page = data['results']
            raw_data.extend(page)
            print('Succes and extended raw_data', next_page_url, '\n')
            
        dataframe = pd.DataFrame(raw_data)  

        dataframe.to_sql(table_name, engine, if_exists ='replace') 
    else:
        print(f"Error status{response.status_code}")

 
if __name__ == "__main__":
    build_starwars_db()