# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('SophiaDB.db')

cursor = conn.cursor()

conn.close()
