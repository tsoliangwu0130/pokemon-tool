# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3


class PokemonScrapyPipeline(object):
	def open_spider(self, spider):
		self.conn = sqlite3.connect('pokemon.sqlite')
		self.cur  = self.conn.cursor()
		self.cur.execute("""
			CREATE TABLE IF NOT EXISTS POKEMONS(
				nationalNumber INTEGER PRIMARY KEY,
				pokemonName TEXT,
				pokemonTypes TEXT,
				gender TEXT,
				eggCycle TEXT,
				eggGroup TEXT,
				pokemonAbilities TEXT,
				catchRate TEXT,
				pokemonStats TEXT,
				evolution TEXT,
				lvMoves TEXT,
				eggMoves TEXT,
				tutorMoves TEXT,
				preEvlMoves TEXT,
				hmMoves TEXT,
				tmMoves TEXT,
				transferMoves TEXT,
				location TEXT
			)""")

	def close_spider(self, spider):
		self.conn.commit()
		self.conn.close()

	def process_item(self, item, spider):
		col         = ','.join(item.keys())
		placeholder = ','.join(len(item) * '?')
		sql         = """
			INSERT INTO POKEMONS({})
			VALUES({})
		"""
		self.cur.execute(sql.format(col, placeholder), item.values())
		return item


class MovesScrapyPipeline(object):
	def open_spider(self, spider):
		self.conn = sqlite3.connect('moves.sqlite')
		self.cur  = self.conn.cursor()
		self.cur.execute("""
			CREATE TABLE IF NOT EXISTS MOVES(
				id INTEGER PRIMARY KEY AUTOINCREMENT,
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
		col         = ','.join(item.keys())
		placeholder = ','.join(len(item) * '?')
		sql         = """
			INSERT INTO MOVES({})
			VALUES({})
		"""
		self.cur.execute(sql.format(col, placeholder), item.values())
		return item
