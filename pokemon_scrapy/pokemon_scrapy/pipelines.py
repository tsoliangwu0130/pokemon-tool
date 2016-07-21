# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3


class MovesScrapyPipeline(object):
	def open_spider(self, spider):
		self.conn = sqlite3.connect('moves.sqlite')
		self.cur  = self.conn.cursor()
		self.cur.execute("""
			CREATE TABLE IF NOT EXISTS MOVES(
				moveName TEXT,
				moveType TEXT,
				moveCate TEXT,
				movePower INTEGER,
				moveAcc INTEGER,
				movePP INTEGER,
				moveTM TEXT,
				moveEffect TEXT,
				moveProb INTEGER
			)""")

	def close_spider(self, spider):
		self.conn.commit()
		self.conn.close()

	def process_item(self, item, spider):
		return item
