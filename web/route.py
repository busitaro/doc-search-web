from flask import request, render_template, jsonify

from .app import app
from .display import page_title, keyname, table_column_list, table_width_list, search_doc_list, get_doc_paths


@app.route('/')
def index():
    """
    検索画面表示

    """
    return render_template('index.html', 
                            page_title=page_title(), 
                            keyname=keyname(),
                            table_column_list=table_column_list(),
                            table_width_list=table_width_list())


@app.route('/update-file-list', methods=['POST'])
def list_order_file():
    """
    検索キーにマッチしたファイルリストを取得

    """
    try:
        search_word = request.form['key']
        return jsonify({'docs': search_doc_list(search_word)})
    except Exception as ex:
        return jsonify({'error': str(ex)})


@app.route('/get-file-list', methods=['POST'])
def get_file_list():
    """
    指定キーのファイルへのリンクパスリストを取得

    """
    try:
        search_key = request.form['key']
        return jsonify({'docpaths': get_doc_paths(search_key)})
    except Exception as ex:
        return jsonify({'error': str(ex)})
