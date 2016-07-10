import scrapy
from bs4 import BeautifulSoup


class PokemonCrawler(scrapy.Spider):
	name = 'pokemon_crawler'
	start_urls = ['http://mpokemon.com/en/oras/pokemon.php?no=1']

	def parse(self, response):
		res = BeautifulSoup(response.body, "lxml")
		for pokemon in res.select('#area'):
			print pokemon
