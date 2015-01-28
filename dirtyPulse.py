#/bin/bash/python

import MySQLdb

temp = open('game_08.31.12.tmp.csv', 'r')

newTable = "CREATE TABLE %s (number INT, name VARCHAR(30), startTime VARCHAR(13), minHR INT, avgHR INT, maxHR INT, inZ1" 

def parsePulse():
	for line in temp:
		tLine = line.split(',')
		if tLine[0] != '':
			print tLine
			nLine = temp.readline()
			nLine = nLine.split(',')
			print nLine
			#make new table
		elif tLine[1].find('Warmup') > 0:
			#print tLine[1].strip()
			#make Warmup row
			pass
		elif tLine[1].find('First Half') > 0:
			#print tLine[1].strip()
			#make First Half row
			pass
		elif tLine[1].find('2nd Half') > 0:
			#print tLine[1].strip()
			#make Second Half row
			pass
		elif tLine[1].find('Overtime') > 0:
			#print tLine[1].strip()
			#make Overtime row
			pass
		else:
			#print "Other facts"
			#insert facts about section of game
			pass

parsePulse()
