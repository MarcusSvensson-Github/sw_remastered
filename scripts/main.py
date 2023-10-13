import ingestion 
import intermediate

api_resources = ['films', 'planets', 'characters', 'starships', 'vehicles', 'species']
ingestion.build_starwars_db(api_resources)
intermediate.create_int_bridges()
