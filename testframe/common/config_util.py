# coding=utf-8
import io
import yaml
import configparser
from config.setting import BASE_DIR, TEST_CONFIG


class ConfigUtil(object):

    @classmethod
    def get_ini(cls, section, option):
        con = configparser.ConfigParser()
        con.read(TEST_CONFIG, encoding='utf-8')
        return con.get(section, option)

    @classmethod
    def get_ini_dict(cls, section, option):
        con = configparser.ConfigParser()
        con.read(TEST_CONFIG, encoding='utf-8')
        v = con.get(section, option)
        return eval(v)

    @classmethod
    def get_yml_all(cls, path):
        """
        :param path: '/config/test.yml'
        :return: 获取配置文件中的配置，返回string
        """
        filepath = BASE_DIR + path
        return yaml.load(io.open(filepath, 'r', encoding='utf-8'), Loader=yaml.FullLoader)

    @classmethod
    def get_yml(cls, path, section, option=''):
        """获取配置文件中的配置，返回string"""
        filepath = BASE_DIR + path
        config = yaml.load(io.open(filepath, 'r', encoding='utf-8'), Loader=yaml.FullLoader)
        if option:
            result = config[section][option]
        else:
            result = config[section]
        return str(result) if isinstance(result, (str, int)) else result

    @classmethod
    def get_yml_int(cls, path, section, option=''):
        """获取配置文件中的配置，返回int"""
        filepath = BASE_DIR + path
        config = yaml.load(io.open(filepath, 'r', encoding='utf-8'), Loader=yaml.FullLoader)
        if option:
            return int(config[section][option])
        else:
            return int(config[section])
