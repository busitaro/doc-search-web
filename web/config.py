import json
from os import path, strerror
from errno import ENOENT


file_path = 'conf'
config_file = 'config.json'


class Config():
    def __init__(self):
        path_to_config_file = '{}/{}'.format(file_path, config_file)
        if not path.exists(path_to_config_file):
            raise FileNotFoundError(ENOENT, strerror(ENOENT), path_to_config_file)
        json_file = open(path_to_config_file, 'r', encoding='utf-8')
        self.__json = json.load(json_file)

    @property
    def page_title(self):
        key = 'page_title'
        return self.__json[key]

    @property
    def directorys(self):
        root_key = 'docroot'
        path_key = 'docpath'
        doc_root = self.__json[root_key]
        docpath_list = self.__json[path_key]

        return list(map(lambda docpath: doc_root + docpath, docpath_list))

    @property
    def key_regexes(self):
        key = 'key_regex'
        return self.__json[key]

    @property
    def keyname(self):
        key = 'keyname'
        return self.__json[key]

    @property
    def docnames(self):
        key = 'docname'
        return self.__json[key]

    @property
    def docpath(self):
        key = 'docpath'
        return self.__json[key]

    @property
    def table_width(self):
        key = 'table_width'
        return self.__json[key]

    @property
    def display_count(self):
        key = 'display_count'
        return self.__json[key]
