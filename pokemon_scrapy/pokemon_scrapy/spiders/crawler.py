import scrapy
from bs4 import BeautifulSoup
from pokemon_scrapy.items import PokemonScrapyItem
from pokemon_scrapy.items import PokemonMovesScrapyItem


class PokemonCrawler(scrapy.Spider):
	name       = 'pokemon_crawler'
	start_urls = ['http://pokemondb.net/pokedex/national']

	def parse(self, response):
		domain      = 'http://pokemondb.net'
		soup        = BeautifulSoup(response.body, "lxml")

		for pokemon in soup.select('.infocard-tall'):
			pokemonURL = domain + pokemon.a.attrs['href']
			yield scrapy.Request(pokemonURL, self.parse_detail)

	def parse_detail(self, response):
		pokemonItem                     = PokemonScrapyItem()
		soup                            = BeautifulSoup(response.body, "lxml")
		pokemonItem['pokemonName']      = soup.select('.svtabs-tab')[0].text
		pokemonItem['nationalNumber']   = soup.select('.vitals-table')[0].tbody.findAll('tr')[0].td.text
		pokemonItem['catchRate']        = soup.select('.vitals-table')[1].tbody.findAll('tr')[1].td.text
		pokemonItem['gender']           = soup.select('.vitals-table')[2].tbody.findAll('tr')[1].td.text
		pokemonItem['eggCycle']         = soup.select('.vitals-table')[2].tbody.findAll('tr')[2].td.text
		pokemonItem['pokemonTypes']     = []
		pokemonItem['pokemonAbilities'] = []
		pokemonItem['eggGroup']         = []
		# pokemonItem['evolution']        = []
		pokemonItem['eggMoves']         = []
		pokemonItem['tutorMoves']       = []
		pokemonItem['hmMoves']          = []
		pokemonItem['tmMoves']          = []
		pokemonItem['transferMoves']    = []
		pokemonItem['preEvlMoves']      = []
		pokemonItem['pokemonStats']     = dict()
		pokemonItem['lvMoves']          = dict()
		pokemonItem['location']         = dict()

		for item in soup.select('.vitals-table')[0].tbody.findAll('tr')[1].td.findAll('a'):
			pokemonItem['pokemonTypes'].append(item.text)

		for item in soup.select('.vitals-table')[0].tbody.findAll('tr')[5].td.findAll('a'):
			pokemonItem['pokemonAbilities'].append(item.text)  # last one is hidden ability

		for item in soup.select('.vitals-table')[2].tbody.findAll('tr')[0].td.findAll('a'):
			pokemonItem['eggGroup'].append(item.text)

		pokemonItem['pokemonStats']['hp']        = soup.select('.vitals-table')[3].tbody.findAll('tr')[0].findAll('td')[0].text
		pokemonItem['pokemonStats']['attack']    = soup.select('.vitals-table')[3].tbody.findAll('tr')[1].findAll('td')[0].text
		pokemonItem['pokemonStats']['defense']   = soup.select('.vitals-table')[3].tbody.findAll('tr')[2].findAll('td')[0].text
		pokemonItem['pokemonStats']['spAttack']  = soup.select('.vitals-table')[3].tbody.findAll('tr')[3].findAll('td')[0].text
		pokemonItem['pokemonStats']['spDefense'] = soup.select('.vitals-table')[3].tbody.findAll('tr')[4].findAll('td')[0].text
		pokemonItem['pokemonStats']['speed']     = soup.select('.vitals-table')[3].tbody.findAll('tr')[5].findAll('td')[0].text
		pokemonItem['pokemonStats']['total']     = soup.select('.vitals-table')[3].tfoot.tr.td.text

		if soup.select('.infocard-evo-list') != []:
			for index, item in enumerate(soup.select('.infocard-evo-list')[0].findAll('span')):
				if index % 2 == 0:
					# pokemonItem['evolution'].append(item.small.text[1:])
					pass
				else:
					evlLv = item.text[12:14]
					if evlLv[-1] == ')':
						evlLv = evlLv[0]
					# pokemonItem['evolution'].append(evlLv)
					pass

		for dataTable in soup.select('.data-table'):
			preSiblings = dataTable.previous_siblings
			for preSibling in preSiblings:
				if preSibling.name == 'h3':
					if preSibling.text == "Moves learnt by level up":
						for item in dataTable.tbody.findAll('tr'):
							pokemonItem['lvMoves'][item.findAll('td')[0].text] = item.findAll('td')[1].text

					elif preSibling.text == "Move Tutor moves":
						for item in dataTable.tbody.findAll('tr'):
							pokemonItem['tutorMoves'].append(item.td.text)

					elif preSibling.text == "Pre-evolution moves":
						for item in dataTable.tbody.findAll('tr'):
							pokemonItem['preEvlMoves'].append(item.td.text)

					elif preSibling.text == "Egg moves":
						for item in dataTable.tbody.findAll('tr'):
							pokemonItem['eggMoves'].append(item.td.text)

					elif preSibling.text == "Moves learnt by TM":
						for item in dataTable.tbody.findAll('tr'):
							pokemonItem['tmMoves'].append(item.findAll('td')[1].text)

					elif preSibling.text == "Moves learnt by HM":
						for item in dataTable.tbody.findAll('tr'):
							pokemonItem['hmMoves'].append(item.findAll('td')[1].text)

					elif preSibling.text == "Transfer-only moves":
						for item in dataTable.tbody.findAll('tr'):
							pokemonItem['transferMoves'].append(item.td.text)
					break

		pokemonItem['tutorMoves']    = list(set(pokemonItem['tutorMoves']))
		pokemonItem['preEvlMoves']   = list(set(pokemonItem['preEvlMoves']))
		pokemonItem['eggMoves']      = list(set(pokemonItem['eggMoves']))
		pokemonItem['tmMoves']       = list(set(pokemonItem['tmMoves']))
		pokemonItem['hmMoves']       = list(set(pokemonItem['hmMoves']))
		pokemonItem['transferMoves'] = list(set(pokemonItem['transferMoves']))

		if soup.select('#dex-locations')[0].parent.select('.vitals-table') != []:
			for item in soup.select('.vitals-table')[5].tbody.findAll('tr'):
				pokemonItem['location'][item.th.text] = item.td.text

		return pokemonItem


class MoveCrawler(scrapy.Spider):
	name       = 'move_crawler'
	start_urls = ['http://pokemondb.net/move/all']

	def parse(self, response):
		soup             = BeautifulSoup(response.body, "lxml")
		moves            = soup.select('#moves')[0].find('tbody').findAll('tr')
		pokemonMovesItem = PokemonMovesScrapyItem()

		for move in moves:
			pokemonMovesItem['moveName']   = move.findAll('td')[0].text
			pokemonMovesItem['moveType']   = move.findAll('td')[1].text
			pokemonMovesItem['moveCate']   = move.findAll('td')[2].text
			pokemonMovesItem['movePower']  = move.findAll('td')[3].text
			pokemonMovesItem['moveAcc']    = move.findAll('td')[4].text
			pokemonMovesItem['movePP']     = move.findAll('td')[5].text
			pokemonMovesItem['moveTM']     = move.findAll('td')[6].text
			pokemonMovesItem['moveEffect'] = move.findAll('td')[7].text
			pokemonMovesItem['moveProb']   = move.findAll('td')[8].text

			yield pokemonMovesItem
