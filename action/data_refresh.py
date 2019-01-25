# -*- coding: utf-8 -*-

import menu
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListView, QMessageBox
from PyQt5.QtCore import QStringListModel
from db import db_dao as dao

class DataFresh(object):
    def re_property(selt, ui):
        tuple_lst = dao.DbDao().get_property_lst()
        lst = map(lambda t: str(t[0]) + " " * 16 + str(t[1]), tuple_lst)
        slm = QStringListModel()
        slm.setStringList(lst)
        ui.lst_property.setModel(slm)

    def re_item(self, ui):
        tuple_lst = dao.DbDao().get_item_lst()
        lst = map(lambda t: str(t[0]) + " " * 16 + str(t[1]), tuple_lst)
        slm = QStringListModel()
        slm.setStringList(lst)
        ui.lst_item.setModel(slm)
