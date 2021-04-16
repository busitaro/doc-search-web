# doc_search_web
有るキーに紐づいた、ドキュメントを検索するシステム  

例:  
ディレクトリ1: 注文書_123.pdf, 注文書_456.pdf  
ディレクトリ2: 納品書_012.pdf, 納品書_123.pdf  

キー: 123で検索 → 注文書_123.pdf, 納品書_123.pdfを抽出

# Usage

## 準備
設定ファイルの設定  
<br>
conf/config.json
|項目名|種別|設定内容|
|:---|:---|:---|
|page_title|文字列|WEBページのタイトル|
|doocname|リスト|ドキュメント名(docディレクトリ毎に指定)
|docroot|文字列|ドキュメント格納ディレクトリのルートディレクトリ|
|docpath|リスト|ルートディレクトリを基準とした、各ドキュメントの格納先|
|keyname|文字列|キーの名称|
|key_regex|リスト|ファイル名からキーを抽出するための正規表現のリスト(docディレクトリ毎に指定)|
|table_width|リスト|WEBページ上のテーブル幅|
|display_count|数値|WEBページ上への最大表示件数|
<br>

infra_conf/default.conf
```conf
root /your/doc/root_folder/path;
```

## 起動
docker-compose up -d

# Author
* busitaro
* busitaro10@gmail.com
