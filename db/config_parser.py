import yaml

with open("db/config.yml", "r") as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)


DBNAME = config.get('DBNAME')
USERNAME = config.get('USERNAME')
HOST = config.get('HOST')
PASSWORD = config.get('PASSWORD')
