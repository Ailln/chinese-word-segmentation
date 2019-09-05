import yaml


def get_default_conf():
    default_config_path = "./datas/conf.yaml"
    with open(default_config_path, "r") as f_conf:
        conf = yaml.load(f_conf.read(), yaml.FullLoader)
    return conf
