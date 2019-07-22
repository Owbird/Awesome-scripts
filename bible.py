#	This script reads the entire NKJV bible
#	to find:
#	- Total number of books
#	- Total number of chapters
#	- Total number of verses
#	- Short verses
#	- Long verses
#	- Words and the total number of appearance
#	- Longest verse
#	- Shortest verse
#	and writes them to a text file
#	For more discoveries visit the author @ github.com/owbird/Discoveries

import json
import operator
from string import punctuation

class Bible(object):

	def __init__(self):

		# setting total books,chapters and verses to 0
		self.totalBooks = 0
		self.totalChapters = 0
		self.totalVerses = 0

		# a list to hold short and long verses
		self.shortVerses = []
		self.longVerses = [] 

		# dictionary to count the verses
		self.wordsCount = {}

		# shortest and longest verse goes here
		self.shortestVerse = ''
		self.longestverse = ''

		# reading the bible
		with open('Bible.json') as bible:

			# converting to json
			bible = json.loads(bible.read())

			# looping through all books
			for i in range(0, 66):

				# getting the chapter number
				chapterNum = 0

				# getting contents
				totself = bible['books'][i]
				
				# getting book
				book = totself['name']

				# increasing total number of books
				self.totalBooks += 1

				# looping through all chapters
				for n in range(0, 200):
					
					# validating verse
					try:
						
						chapter = totself['chapters'][n]
					
					except IndexError:
					
						continue

					# increasing current chapter of current book
					chapterNum += 1

					# increasing total number of chapters
					self.totalChapters += 1
					
					# going through all verses
					for p in range(0, 200):

						# validating verses
						try:
							verse = chapter['verses'][p]['text']
							verseNum = chapter['verses'][p]['num']

							# getting long and short verses
							if len(verse) < 50:
							
								self.shortVerses.append((book, chapterNum, verseNum, verse))
							
							if len(verse) < 300:
							
								self.longVerses.append((book, chapterNum, verseNum, verse))
							
							for punc in punctuation:
								
								if punc in verse:
								
									# eliminating them
									verse = verse.replace(punc, ' ')
							
							# separating words
							words = verse.split(' ')
						
							# going through words
							for word in words:
							
								# with the exception of God
								if word == 'God':
									
									word = 'God'
									
								else:
								
									# creating lowercase letters
									word = word.lower()
									
								# creating a key for each
								self.wordsCount.setdefault(word, 0)
								
								# counting the words
								if word in self.wordsCount.keys():
										
								    self.wordsCount[word] += 1

						except IndexError:
							
							continue

						# increasing total number of verses
						self.totalVerses += 1

		# limit for longest verse		
		longest = 100

		# going through saved long verses
		for long in self.longVerses:

			# if verse meets requirements
			if len(long[3]) > longest:

				# new limit = the verse
				longest = len(long[3])

				# longest verse = that verse
				self.longestverse = long

		# limit for shortest verse
		shortest = 100

		# going through saved short verses
		for short in self.shortVerses:

			# if verse meets requirements
			if len(short[3]) < shortest:

				# new limit = the verse
				shortest = len(short[3])
				
				# shortest verse = that verse
				self.shortestVerse = short

		# creating a file
		with open('bible.txt','w') as db:

			# saving to file
			txt = f'Version: NKJV\n\nTotal books: {self.totalBooks}\n\nTotal chapters: {self.totalChapters}\n\nTotal verses: {self.totalVerses}\n\nTotal words: {sum([_ for _ in self.wordsCount.values()])}\n\nShortest verse: {self.shortestVerse}\n\nlongest verse: {self.longestverse}\n\n'

			db.write(txt)

			db.write('==Short verses==\n\n')

			# going through saved short verses
			for i, short in enumerate(self.shortVerses):
				
				# changing from tuple to string
				short = ''.join(f'{short}')

				# saving to file
				db.write(f'{i}) {short}\n\n')

			db.write('==All words==\n\n')

			# counting the words
			for key, value in sorted(self.wordsCount.items(), key = operator.itemgetter(1), reverse = True):

				# calculating the percentage value
				per = round(value / sum([_ for _ in self.wordsCount.values()]) * 100,3)

				# saving to file
				db.write(f'{key} => {value} => {per}%\n\n')

bible = Bible()
