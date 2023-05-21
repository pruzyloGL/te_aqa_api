import os
import json


class Config():
    DEFAULT_ENV = 'prod'

    @staticmethod
    def get_property(name):
        # define the env
        target = os.environ.get('TARGET', Config.DEFAULT_ENV)
        # target = os.environ['TARGET']

        # read the proper json file
        path_to_config = f"./env_config/{target}.json"
        with open(path_to_config) as f:
            config_from_json = json.load(f)
        
        # get the property name from parameter 'name'
        value = config_from_json.get(name)

        return value