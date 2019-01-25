# -*- coding: utf-8 -*-

import sqlite3 as db

conn = db.connect('data.db', timeout=5)

cursor = conn.cursor()

cursor.execute('create table property (str int(4), agi int(4), int int(4), cost_yaer int(3), max_year int(3))')

cursor.close()

conn.commit()

conn.close()