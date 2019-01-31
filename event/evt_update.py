# -*- coding: utf-8 -*-

from db import db_dao


class Update(object):

    def __init__(self):
        self.dao = db_dao.DbDao()

    def time_add(self, num):
        self.dao.update_time(num)
