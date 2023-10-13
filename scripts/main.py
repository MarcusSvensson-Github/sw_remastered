import ingestion 
import intermediate

api_resources = ['films', 'planets', 'starships', 'vehicles', 'species']
ingestion.build_starwars_db(api_resources)
intermediate.create_intermediate_bridges(api_resources)
