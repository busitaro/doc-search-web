from os import path, listdir
from re import search

from .config import Config


config = Config()


def get_keys_by_directory(search_word: str) -> list:
    """
    docの格納directory毎に
    検索ワードにマッチしたキーの一覧を取得する

    Params
    -------
    search_word: str
        検索ワード

    Returns
    -------
    0: list
        ディレクトリ毎の検索マッチしたキー一覧
        [[ディレクトリ1でマッチしたキーのリスト], [ディレクトリ2でマッチしたキーのリスト], ...]
    """
    keys_by_directory = list()

    for idx, directory in enumerate(config.directorys):
        key_list = search_file_in_directory(directory, search_word, config.key_regexes[idx], by_key=True)
        keys_by_directory.append(key_list)
    return keys_by_directory


def get_filename_by_directory(search_key: str) -> list:
    """
    docの格納directory毎に
    キーが検索キーに一致したファイルの一覧を取得する

    Params
    ---------
    search_key: str
        検索キー

    Returns
    ---------
    0: list
        各ディレクトリ毎に検索キーにキーが一致したdocのリスト
        ヒットファイルが無いディレクトリに対しては""が設定される
        ['dir1のヒットファイル', 'dir2のヒットファイル', ...]
    """
    filename_by_directory = list()

    for idx, directory in enumerate(config.directorys):
        file_list = search_file_in_directory(directory, search_key, config.key_regexes[idx], by_key=False)
        filename_by_directory.append(file_list)
    return filename_by_directory


def search_file_in_directory(search_path: str, search_word: str, key_regex: str, by_key: bool = False) -> list:
    """
    指定ディレクトリのファイル名を
    正規表現にて抽出し、
    検索ワードに前方一致するもののリストを取得

    リストはタイムスタンプ順の新しい順で、
    最大取得件数はConfigのdisplay_countとする

    Params
    --------
    search_path: str
        検索するディレクトリ
    search_word: str
        検索ワード
    key_regex: str
        キー抽出正規表現
    by_key: bool
        True: キーの一覧(正規表現による抽出結果 )を取得
        False: ファイル名の一覧を取得

    Returns
    --------
    0: list
        取得内容のリスト
    """
    # ディレクトリの存在チェック
    if not path.exists(search_path):
        raise FileNotFoundError('ディレクトリが存在しません。')

    # ファイル一覧をタイムスタンプでソートし取得
    filename_list = \
        sorted(listdir(search_path), 
                    key=lambda f: path.getmtime('{}/{}'.format(search_path, f)), reverse=True)

    # key: ファイル名のdictを作成
    key_name_dict = dict()
    for filename in filename_list:
        key = search(key_regex, filename)
        if key is None:
            # 正規表現に一致しないファイルは飛ばす
            continue
        key = key.group()
        # key重複を起こしている場合、例外を発生させる
        if key in key_name_dict.keys():
            raise ValueError('同一keyのファイルが複数存在します。')
        key_name_dict[key] = filename

    if search_word:
        # keyに対して、search_wordでfilter（前方一致）
        key_name_dict = {key: value for key, value in 
                filter(lambda kv: kv[0][:len(search_word)] == search_word, key_name_dict.items())}

    # 取得内容に応じてリスト作成
    if by_key:
        ret_list = list(key_name_dict.keys())
    else:
        ret_list = list(key_name_dict.values())

    return ret_list[:config.display_count]
