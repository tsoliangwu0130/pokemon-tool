# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PokemonScrapyItem(scrapy.Item):
	pokemonName      = scrapy.Field()
	nationalNumber   = scrapy.Field()
	pokemonTypes     = scrapy.Field()
	gender           = scrapy.Field()
	eggCycle         = scrapy.Field()
	eggGroup         = scrapy.Field()
	pokemonAbilities = scrapy.Field()
	catchRate        = scrapy.Field()
	pokemonStats     = scrapy.Field()
	# evolution        = scrapy.Field()
	lvMoves          = scrapy.Field()
	eggMoves         = scrapy.Field()
	tutorMoves       = scrapy.Field()
	preEvlMoves      = scrapy.Field()
	hmMoves          = scrapy.Field()
	tmMoves          = scrapy.Field()
	transferMoves    = scrapy.Field()
	location         = scrapy.Field()


class PokemonMovesScrapyItem(scrapy.Item):
	moveName   = scrapy.Field()
	moveType   = scrapy.Field()
	moveCate   = scrapy.Field()
	movePower  = scrapy.Field()
	moveAcc    = scrapy.Field()
	movePP     = scrapy.Field()
	moveTM     = scrapy.Field()
	moveEffect = scrapy.Field()
	moveProb   = scrapy.Field()
