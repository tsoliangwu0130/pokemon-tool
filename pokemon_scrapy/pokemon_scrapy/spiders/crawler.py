import scrapy
from bs4 import BeautifulSoup


class PokemonCrawler(scrapy.Spider):
	name       = 'pokemon_crawler'
	start_urls = ['http://pokemondb.net/pokedex/national']

	def parse(self, response):
		domain      = 'http://pokemondb.net'
		soup        = BeautifulSoup(response.body, "lxml")
		pokemonList = soup.select('.infocard-tall')

		for pokemon in pokemonList:
			pokemonURL = domain + pokemon.a.attrs['href']
			print pokemonURL

		print len(pokemonList), "Pokemons found."
