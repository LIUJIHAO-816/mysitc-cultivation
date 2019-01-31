# -*- coding: utf-8 -*-

import sqlite3 as db


class DbDao(object):

    def init_table(self):
        conn = db.connect('data.db', timeout=5)
        cursor = conn.cursor()
        cursor.execute(
            'create table if not exists property (code varchar(10), name varchar(20), now_value int(4), max_value int(4), area int(1))')
        cursor.execute(
            'create table if not exists consum (code varchar(10), name varchar(20), number int(3), function varchar(3), description varchar(255))')
        cursor.execute(
            'create table if not exists skill (code varchar(10), name varchar(20), owned boolean(1),function varchar(3), description varchar(255), limited varchar(255), get_rate int(3))')
        cursor.execute(
            'create table if not exists maps (code varchar(10), type varchar(4), name varchar(20), cost int(2), description varchar(255), condition varchar(255), call varchar(255))')
        cursor.close()
        conn.commit()
        conn.close()

    def init_data(self):
        conn = db.connect('data.db', timeout=5)
        cursor = conn.cursor()

        c = cursor.execute(
            'select count(*) from property')
        count = c.fetchone()[0]
        if count <= 0:
            cursor.executemany('insert into property values(?,?,?,?,?)', [
                ('str', '力量', 5, 9999, 1),
                ('agi', '灵敏', 5, 9999, 1),
                ('int', '智慧', 5, 9999, 1),
                ('luk', '幸运', 0, 50, 1),
                ('sav', '悟性', 0, 50, 1),
                ('time', '修炼时间', 0, 100, 2)
            ])
        c = cursor.execute(
            'select count(*) from consum')
        count = c.fetchone()[0]
        if count <= 0:
            cursor.executemany('insert into consum values(?,?,?,?,?)', [
                ('consum1', '后悔丸', '0', 'A', '撤销上次的属性变化，10%失败（成功时无法连续使用）'),
                ('consum2', '天生药', '0', 'B', '下次副本无视条件且通过率+10~20%（重复使用只看作一次）'),
                ('consum3', '灵魂枣', '0', 'C', '所有基础属性基于当前值增加3~8%，有1%出现5倍效果'),
                ('consum4', '时间翅', '0', 'D', '修炼时间上限+1~2，有1%使得上限-1')
            ])
        c = cursor.execute(
            'select count(*) from maps')
        count = c.fetchone()[0]
        if count <= 0:
            cursor.executemany('insert into maps values(?,?,?,?,?,?,?)', [
                ('m1', 'A', '小树林', 1, None, None, None),
                ('m2', 'A', '红枫林', 1, None, None, None),
                ('m3', 'A', '暗夜林地', 1, None, None, None),
                ('m6', 'B', '蓝岩坡', 1, None, None, None),
                ('m7', 'B', '冥灵山', 1, None, None, None),
                ('m8', 'B', '无霞峰', 1, None, None, None),
                ('m11', 'C', '风神窟', 1, None, None, None),
                ('m12', 'C', '天鹰洞', 1, None, None, None),
                ('m13', 'C', '三神殿', 1, None, None, None),
            ])
        cursor.close()
        conn.commit()
        conn.close()

    def truncate_tbl(self):
        conn = db.connect('data.db', timeout=5)
        cursor = conn.cursor()
        cursor.execute("delete from property")
        cursor.execute("delete from consum")
        cursor.execute("delete from skill")
        cursor.close()
        conn.commit()
        conn.close()

    def get_property_lst(self):
        conn = db.connect('data.db', timeout=5)
        cursor = conn.cursor()
        c = cursor.execute("select name, now_value from property where area = 1")
        result = c.fetchall()
        cursor.close()
        conn.commit()
        conn.close()
        return result

    def get_time_cost(self):
        conn = db.connect('data.db', timeout=5)
        cursor = conn.cursor()
        c = cursor.execute("select now_value, max_value from property where area = 2")
        result = c.fetchone()
        cursor.close()
        conn.commit()
        conn.close()
        return result

    def get_item_lst(self):
        conn = db.connect('data.db', timeout=5)
        cursor = conn.cursor()
        c = cursor.execute("select name, number from consum")
        result = c.fetchall()
        cursor.close()
        conn.commit()
        conn.close()
        return result

    def update_single_property(self, code, delta):
        conn = db.connect('data.db', timeout=5)
        cursor = conn.cursor()
        cursor.execute("update property set now_value = now_value + ? where code = ?", (delta, code))
        cursor.close()
        conn.commit()
        conn.close()

    def get_map_list(self, type):
        conn = db.connect('data.db', timeout=5)
        cursor = conn.cursor()
        c = cursor.execute("select name from maps where type = ?", (type,))
        result = c.fetchall()
        cursor.close()
        conn.commit()
        conn.close()
        return result

    def update_time(self, num):
        conn = db.connect('data.db', timeout=5)
        cursor = conn.cursor()
        cursor.execute("update property set now_value = now_value + ? where code = 'time'", (num,))
        cursor.close()
        conn.commit()
        conn.close()
