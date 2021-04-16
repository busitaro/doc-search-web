
let leftTable

const getDocs = (searchWord) => {
  $.ajax({
    url: '/update-file-list',
    type: 'POST',
    dataType: 'json',
    // フォーム要素の内容をハッシュ形式に変換
    data: $('form').serializeArray(),
    timeout: 5000,
  })
  .done(function(data) {
    if ('error' in data) {
      alert(data['error'])
    } else {
      const docs = data['docs']
      // tableの行をすべて削除
      leftTable.clearTable()
      // tableへ追加
      const addData = 
        docs.map((doc, index, _) => {
          const exists = doc.exists.map(exist => {
            return exist === 1 ? '有' : '無'
          })
          return [index + 1, doc.key].concat(exists)
        })
      leftTable.addRow(addData)
    }
  })
  .fail(function() {
      window.confirm('通信に失敗しました。')
  });
}

const openDocs = () => {
  $.ajax({
    url: '/get-file-list',
    type: 'POST',
    dataType: 'json',
    // 選択中のkey
    data: {'key': leftTable.getSelected().childNodes[1].innerHTML},
    timeout: 5000,
  })
  .done(function(data) {
    if ('error' in data) {
      alert(data['error'])
    } else {
      const docpaths = data['docpaths']
      // リンクを開く
      docpaths.forEach(docpath => {
        window.open(docpath)
      })
    }
  })
  .fail(function() {
      window.confirm('通信に失敗しました。')
  });
}

// 選択可能テーブルの設定
$(function () {
  leftTable = new TableControl({
    'table': '#docTable',
  })
})

// 検索
$(function () {
  $('#searchBtn').on('click', () => {
    getDocs()
  })
})

// 開く
$(function () {
  $('#btnOpen').on('click', () => {
    openDocs()
  })
})
