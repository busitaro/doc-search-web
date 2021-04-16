class TableControl {
  constructor (config) {
    this.table = document.querySelector(config.table)
    this.init()
  }

  init () {
    this.selectedClass = 'selected'
    this.setClickListener()
  }

  setClickListener() {
    let trList = Array.from(this.table.querySelectorAll('tr'))
    trList.shift() // 項目名行を削除
    this.addEventListener(trList)
  }

  addEventListener(trList) {
    trList.map((tr) => {
      tr.addEventListener('click', () => {
        this.clearClass(trList)
        tr.classList.add(this.selectedClass)
      })
    })
  }

  clearClass(trList) {
    trList.map((tr) => {
      tr.classList.remove(this.selectedClass)
    })
  }

  addRow (data) {
    data.map ((d) => {
      const newRow = this.table.tBodies[0].insertRow(-1)
      d.map ((td, index, _) => {
        if (index === 0) {
          // 最初のセルはth
          const th = document.createElement('th')
          th.textContent = td
          newRow.appendChild(th)
        } else {
          // 以降のセルはtd
          const newCell = newRow.insertCell(-1)
          newCell.textContent = td
        }
      })
    })
    this.setClickListener()
  }

  clearTable() {
    while (this.table.rows.length > 1) this.table.deleteRow(-1);
  }

  getSelected() {
    return this.table.querySelector('.' + this.selectedClass)
  }
}
