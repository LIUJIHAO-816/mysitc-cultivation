from PyQt5 import QtWidgets

# python cxfreeze e:\pyproject\archive-management\main.py --target-dir E:\myexe --base-name="win32gui"

import sys
import menu_extension
from action import data_refresh as dr
from PyQt5.QtGui import QIcon
from db import db_dao

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = menu_extension.Ui_extension()
    ui.setupUi(widget)
    ui.listener()
    widget.setWindowIcon(QIcon('web.png'))  # 增加icon图标，如果没有图片可以没有这句
    widget.setFixedSize(widget.width(), widget.height())
    widget.show()

    # 初始化数据库
    dao = db_dao.DbDao()
    dao.init_table()
    dao.init_data()

    df = dr.DataFresh()
    df.re_property(ui)
    df.re_item(ui)
    sys.exit(app.exec_())

