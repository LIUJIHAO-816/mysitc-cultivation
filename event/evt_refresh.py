# -*- coding: utf-8 -*-

from PyQt5.QtCore import QStringListModel
from db import db_dao


class Refresh(object):

    def __init__(self):
        self.dao = db_dao.DbDao()

    def re_property(self, ui):
        tuple_lst = self.dao.get_property_lst()
        lst = map(lambda t: str(t[0]) + " " * 10 + str(t[1]), tuple_lst)
        slm = QStringListModel()
        slm.setStringList(lst)
        ui.lst_property.setModel(slm)

    def re_time(self, ui):
        tup = self.dao.get_time_cost()
        text = str(tup[0]) + " " * 2 + "/" + " " * 2 + str(tup[1])
        ui.lbl_time_value.setText(text)

    def re_item(self, ui):
        tuple_lst = self.dao.get_item_lst()
        lst = map(lambda t: str(t[0]) + " " * 12 + str(t[1]), tuple_lst)
        slm = QStringListModel()
        slm.setStringList(lst)
        ui.lst_item.setModel(slm)

    def re_map_list(self, ui, type):
        tuple_lst = self.dao.get_map_list(type)
        lst = map(lambda t: str(t[0]), tuple_lst)
        slm = QStringListModel()
        slm.setStringList(lst)
        ui.lst_sub_map.setModel(slm)
