import scrapy
from bs4 import BeautifulSoup


class PokemonCrawler(scrapy.Spider):
	name       = 'pokemon_crawler'
	# start_urls = ['http://pokemondb.net/pokedex/national']
	start_urls = ['http://pokemondb.net/pokedex/nidoran-m']

	def parse(self, response):
		# domain      = 'http://pokemondb.net'
		# soup        = BeautifulSoup(response.body, "lxml")
		# pokemonList = soup.select('.infocard-tall')

		# for pokemon in pokemonList:
		# 	pokemonURL = domain + pokemon.a.attrs['href']
		# 	yield scrapy.Request(pokemonURL, self.parse_detail)

		soup           = BeautifulSoup(response.body, "lxml")
		pokemonName    = soup.select('.svtabs-tab')[0].text
		nationalNumber = soup.select('.vitals-table')[0].tbody.findAll('tr')[0].td.text

		pokemonTypes = []
		for item in soup.select('.vitals-table')[0].tbody.findAll('tr')[1].td.findAll('a'):
			pokemonTypes.append(item.text)

		pokemonAbilities = []
		for item in soup.select('.vitals-table')[0].tbody.findAll('tr')[5].td.findAll('a'):
			pokemonAbilities.append(item.text)  # last one is hidden ability

		catchRate = soup.select('.vitals-table')[1].tbody.findAll('tr')[1].td.text

		eggGroup = []
		for item in soup.select('.vitals-table')[2].tbody.findAll('tr')[0].td.findAll('a'):
			eggGroup.append(item.text)

		gender   = soup.select('.vitals-table')[2].tbody.findAll('tr')[1].td.text
		eggCycle = soup.select('.vitals-table')[2].tbody.findAll('tr')[2].td.text

		pokemonStats              = {'hp': 0, 'attack': 0, 'defense': 0, 'spAttack': 0, 'spDefense': 0, 'speed': 0, 'total': 0}
		pokemonStats['hp']        = soup.select('.vitals-table')[3].tbody.findAll('tr')[0].findAll('td')[0].text
		pokemonStats['attack']    = soup.select('.vitals-table')[3].tbody.findAll('tr')[1].findAll('td')[0].text
		pokemonStats['defense']   = soup.select('.vitals-table')[3].tbody.findAll('tr')[2].findAll('td')[0].text
		pokemonStats['spAttack']  = soup.select('.vitals-table')[3].tbody.findAll('tr')[3].findAll('td')[0].text
		pokemonStats['spDefense'] = soup.select('.vitals-table')[3].tbody.findAll('tr')[4].findAll('td')[0].text
		pokemonStats['speed']     = soup.select('.vitals-table')[3].tbody.findAll('tr')[5].findAll('td')[0].text
		pokemonStats['total']     = soup.select('.vitals-table')[3].tfoot.tr.td.text

		evolution = []
		for index, item in enumerate(soup.select('.infocard-evo-list')[0].findAll('span')):
			if index % 2 == 0:
				evolution.append(item.small.text[1:])
			else:
				evolution.append(item.text[12:14])

		lvMoves = dict()
		for item in soup.select('.data-table')[0].tbody.findAll('tr'):
			lvMoves[item.findAll('td')[0].text] = item.findAll('td')[1].text

		eggMoves = []
		for item in soup.select('.data-table')[1].tbody.findAll('tr'):
			eggMoves.append(item.td.text)

		tutorMoves = []
		for item in soup.select('.data-table')[2].tbody.findAll('tr'):
			tutorMoves.append(item.td.text)

		hmMoves = []
		for item in soup.select('.data-table')[3].tbody.findAll('tr'):
			hmMoves.append(item.findAll('td')[1].text)

		tmMoves = []
		for item in soup.select('.data-table')[4].tbody.findAll('tr'):
			tmMoves.append(item.findAll('td')[1].text)

		transferMoves = []
		for item in soup.select('.data-table')[5].tbody.findAll('tr'):
			transferMoves.append(item.td.text)

		location = dict()
		for item in soup.select('.vitals-table')[5].tbody.findAll('tr'):
			location[item.th.text] = item.td.text

	# def parse_detail(self, response):
	# 	soup           = BeautifulSoup(response.body, "lxml")
	# 	pokemonName    = soup.select('.svtabs-tab')[0].text
	# 	nationalNumber = soup.select('.vitals-table')[0].tbody.findAll('tr')[0].td.text
		
	# 	print soup.select('.vitals-table')[0].tbody.findAll('tr')[1].findAll('td')