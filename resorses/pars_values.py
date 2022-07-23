import yaml


def getDataFromConfig(key):
    with open('resorses/prod_conf.yaml') as f:
        my_dict = yaml.safe_load(f)
        test_data = my_dict[key]
        return test_data




