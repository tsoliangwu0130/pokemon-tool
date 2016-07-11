import scrapy
from bs4 import BeautifulSoup


class PokemonCrawler(scrapy.Spider):
	name       = 'pokemon_crawler'
	start_urls = ['http://mpokemon.com/en/oras/pokemon.php?no=1']

	def parse(self, response):
		res = BeautifulSoup(response.body, "lxml")
		print res.select('#maincontent')[0].prettify() # pokemon details
		print res.select('#maincontent2')[0].prettify() # available skills
