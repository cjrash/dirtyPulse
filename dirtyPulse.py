#/bin/bash/python

import MySQLdb

temp = open('../../game_08.31.12.tmp.csv', 'r')

#tL = temp.readline()  #get rid of first 4 lines and draw table name (date)
#print tL

inDate = "083112"

newTable = "CREATE TABLE %s (number INT, name VARCHAR(30), startTime VARCHAR(13), minHR INT, avgHR INT, maxHR INT, inZ1t VARCHAR(13), inZ2t VARCHAR(13), inZ3t VARCHAR(13), inZ4t VARCHAR(13), inZ5t VARCHAR(13), abvThrest VARCHAR(13), tLoad INT, kCal INT, maxHRO VARCHAR(15), minHRp VARCHAR(5), avgHRp VARCHAR(5), maxHRp VARCHAR(5), inZ1p VARCHAR(5), inZ2p VARCHAR(5), inZ3p VARCHAR(5), inZ4p VARCHAR(5), inZ5p VARCHAR(5), abvThresp VARCHAR(5), tLoadp VARCHAR(5), kCalp VARCHAR(5))" % inDate 

print newTable

def parsePulse():
	for line in temp:
		tLine = line.split(',')
		if tLine[0] != '':
			print tLine
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
			print tLine
			#insert facts about section of game
			pass

#parsePulse()
