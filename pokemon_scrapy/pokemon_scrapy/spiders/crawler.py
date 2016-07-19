import scrapy
from bs4 import BeautifulSoup


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
		soup             = BeautifulSoup(response.body, "lxml")
		pokemonName      = soup.select('.svtabs-tab')[0].text
		nationalNumber   = soup.select('.vitals-table')[0].tbody.findAll('tr')[0].td.text
		catchRate        = soup.select('.vitals-table')[1].tbody.findAll('tr')[1].td.text
		gender           = soup.select('.vitals-table')[2].tbody.findAll('tr')[1].td.text
		eggCycle         = soup.select('.vitals-table')[2].tbody.findAll('tr')[2].td.text
		pokemonTypes     = []
		pokemonAbilities = []
		eggGroup         = []
		evolution        = []
		eggMoves         = []
		tutorMoves       = []
		hmMoves          = []
		tmMoves          = []
		transferMoves    = []
		preEvlMoves      = []
		pokemonStats     = dict()
		lvMoves          = dict()
		location         = dict()

		for item in soup.select('.vitals-table')[0].tbody.findAll('tr')[1].td.findAll('a'):
			pokemonTypes.append(item.text)

		for item in soup.select('.vitals-table')[0].tbody.findAll('tr')[5].td.findAll('a'):
			pokemonAbilities.append(item.text)  # last one is hidden ability

		for item in soup.select('.vitals-table')[2].tbody.findAll('tr')[0].td.findAll('a'):
			eggGroup.append(item.text)

		pokemonStats['hp']        = soup.select('.vitals-table')[3].tbody.findAll('tr')[0].findAll('td')[0].text
		pokemonStats['attack']    = soup.select('.vitals-table')[3].tbody.findAll('tr')[1].findAll('td')[0].text
		pokemonStats['defense']   = soup.select('.vitals-table')[3].tbody.findAll('tr')[2].findAll('td')[0].text
		pokemonStats['spAttack']  = soup.select('.vitals-table')[3].tbody.findAll('tr')[3].findAll('td')[0].text
		pokemonStats['spDefense'] = soup.select('.vitals-table')[3].tbody.findAll('tr')[4].findAll('td')[0].text
		pokemonStats['speed']     = soup.select('.vitals-table')[3].tbody.findAll('tr')[5].findAll('td')[0].text
		pokemonStats['total']     = soup.select('.vitals-table')[3].tfoot.tr.td.text

		if soup.select('.infocard-evo-list') != []:
			for index, item in enumerate(soup.select('.infocard-evo-list')[0].findAll('span')):
				if index % 2 == 0:
					evolution.append(item.small.text[1:])
				else:
					evlLv = item.text[12:14]
					if evlLv[-1] == ')':
						evlLv = evlLv[0]
					evolution.append(evlLv)

		for dataTable in soup.select('.data-table'):
			preSiblings = dataTable.previous_siblings
			for preSibling in preSiblings:
				if preSibling.name == 'h3':
					if preSibling.text == "Moves learnt by level up":
						for item in dataTable.tbody.findAll('tr'):
							lvMoves[item.findAll('td')[0].text] = item.findAll('td')[1].text

					elif preSibling.text == "Move Tutor moves":
						for item in dataTable.tbody.findAll('tr'):
							tutorMoves.append(item.td.text)

					elif preSibling.text == "Pre-evolution moves":
						for item in dataTable.tbody.findAll('tr'):
							preEvlMoves.append(item.td.text)

					elif preSibling.text == "Egg moves":
						for item in dataTable.tbody.findAll('tr'):
							eggMoves.append(item.td.text)

					elif preSibling.text == "Moves learnt by TM":
						for item in dataTable.tbody.findAll('tr'):
							tmMoves.append(item.findAll('td')[1].text)

					elif preSibling.text == "Moves learnt by HM":
						for item in dataTable.tbody.findAll('tr'):
							hmMoves.append(item.findAll('td')[1].text)

					elif preSibling.text == "Transfer-only moves":
						for item in dataTable.tbody.findAll('tr'):
							transferMoves.append(item.td.text)
					break

		tutorMoves    = list(set(tutorMoves))
		preEvlMoves   = list(set(preEvlMoves))
		eggMoves      = list(set(eggMoves))
		tmMoves       = list(set(tmMoves))
		hmMoves       = list(set(hmMoves))
		transferMoves = list(set(transferMoves))

		if soup.select('#dex-locations')[0].parent.select('.vitals-table') != []:
			for item in soup.select('.vitals-table')[5].tbody.findAll('tr'):
				location[item.th.text] = item.td.text

		print "Pokemon:", pokemonName
		print "National Number:", nationalNumber
		print "Type:", pokemonTypes
		print "Abilities:", pokemonAbilities
		print "catchRate:", catchRate
		print "Base Stats", pokemonStats
		print "Evolution Chain:", evolution
		print "Level Moves:", lvMoves
		print "Egg Moves:", eggMoves
		print "Tutor Moves:", tutorMoves
		print "Pre-evolution moves:", preEvlMoves
		print "HM Moves:", hmMoves
		print "TM Moves:", tmMoves
		print "Transfer only Moves:", transferMoves
		print "Location:", location


class MoveCrawler(scrapy.Spider):
	name       = 'move_crawler'
	start_urls = ['http://pokemondb.net/move/all']

	def parse(self, response):
		soup  = BeautifulSoup(response.body, "lxml")
		moves = soup.select('#moves')[0].find('tbody').findAll('tr')

		pokemonMoves = [[]]
		for move in moves:
			pokemonMove = []
			pokemonMove.append(move.findAll('td')[0].text)
			pokemonMove.append(move.findAll('td')[1].text)
			pokemonMove.append(move.findAll('td')[2].text)
			pokemonMove.append(move.findAll('td')[3].text)
			pokemonMove.append(move.findAll('td')[4].text)
			pokemonMove.append(move.findAll('td')[5].text)
			pokemonMove.append(move.findAll('td')[6].text)
			pokemonMove.append(move.findAll('td')[7].text)
			pokemonMove.append(move.findAll('td')[8].text)
			pokemonMoves.append(pokemonMove)
