# -*- coding: utf-8 -*-

from db import db_dao
from event import evt_refresh, evt_update


class ButtonAction(object):

    def __init__(self):
        self.dao = db_dao.DbDao()
        self.refresh = evt_refresh.Refresh()
        self.update = evt_update.Update()

    def prop_test_1(self, ui):
        self.dao.update_single_property("str", 5)
        self.refresh.re_property(ui)
        self.update.time_add(1)
        self.refresh.re_time(ui)

    def restart(self, ui):
        self.dao.truncate_tbl()
        self.dao.init_data()
        self.refresh.re_property(ui)
        self.refresh.re_item(ui)
        self.refresh.re_time(ui)

    def show_map_a_list(self, ui):
        self.refresh.re_map_list(ui, 'A')

    def show_map_b_list(self, ui):
        self.refresh.re_map_list(ui, 'B')

    def show_map_c_list(self, ui):
        self.refresh.re_map_list(ui, 'C')
