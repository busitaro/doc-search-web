from .config import Config
from .file import get_keys_by_directory, get_filename_by_directory


config = Config()


def page_title() -> str:
    """
    設定ファイルから、ページタイトルを取得

    Returns
    -------
    0: str
        ページタイトル
    """
    return config.page_title


def keyname() -> str:
    """
    設定ファイルから、キー名を取得

    Returns
    -------
    0: str
        キー名
    """
    return config.keyname


def table_column_list() -> list:
    """
    テーブルカラム名のリストを生成する

    Returns
    -------
    0: list
        テーブルカラム名のリスト
    """
    keyname = config.keyname
    docnames = config.docnames
    table_columns = [keyname] + docnames

    return table_columns


def table_width_list() -> list:
    """
    テーブル幅のリストを生成する

    Returns
    -------
    0: list
        テーブル幅のリスト
    """
    return config.table_width


def search_doc_list(search_word: str) -> list:
    """
    search_wordにヒットする各key毎にそれぞれのdocが存在するかを判定

    Params
    -------
    search_word: str
        検索ワード

    Returns
    -------
    0: list
        各要素は辞書(key: 文書キー、 value: 各文書が存在するかのリスト)
    """
    # directory毎にsearch_wordにヒットするkeyのリストを取得
    keys_by_directory = get_keys_by_directory(search_word)

    # 取得したkeyの一覧を重複無しで取得する
    key_set = set()
    for key_list in keys_by_directory:
        key_set = key_set | set(key_list)
    # displayのmax分に絞る
    key_list = list(key_set)[:config.display_count]

    # 各keyについて、それぞれのdocが存在するか判定(1: 存在、 0:存在しない)
    doc_list = list()
    for key in key_list:
        exists_file_list = \
            [int(key in key_list) for key_list in keys_by_directory]
        doc_list.append({'key': key, 'exists': exists_file_list})

    return doc_list


def get_doc_paths(search_key: str) -> list:
    """
    search_keyの文書のパスを取得する

    Params
    -------
    search_key: str
        検索キー

    Returns
    -------
    0: list
        文書パスのリスト
    """
    doc_list_by_directory = get_filename_by_directory(search_key)

    # ディレクトリ毎に1件以下のファイルがヒットしていることを確認
    doc_list = list()
    for docs in doc_list_by_directory:
        doc_count = len(docs)
        if doc_count > 1:
            raise ValueError('同一keyのファイルが複数存在します。')
        elif doc_count == 1:
            doc_list.append(docs[0])
        else:
            doc_list.append('')

    # パスを生成
    path_list = ['{}/{}'.format(config.docpath[idx], doc) for idx, doc in enumerate(doc_list) if doc != '']

    return path_list
