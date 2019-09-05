from utils import conf_utils

conf = conf_utils.get_default_conf()


def read_data(data_path):
    with open(data_path, "r") as f_data:
        datas = f_data.readlines()
    return datas


def get_datas():
    train_path = conf["dataset"]["train_path"]
    test_path = conf["dataset"]["test_path"]
    train_datas = read_data(train_path)
    test_datas = read_data(test_path)
    return train_datas, test_datas
