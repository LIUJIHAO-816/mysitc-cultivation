# -*- coding: utf-8 -*-

from db import db_dao as dao
from action import data_refresh as dr


class ButtonAction(object):

    def prop_test_1(self, ui):
        dao.DbDao().update_single_property("str", 5)
        dr.DataFresh().re_property(ui)

    def show_map_A_list(self, ui):
        dr.DataFresh().re_map_list(ui, 'A')

    def show_map_B_list(self, ui):
        dr.DataFresh().re_map_list(ui, 'B')

    def show_map_C_list(self, ui):
        dr.DataFresh().re_map_list(ui, 'C')
