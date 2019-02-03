#Distance Between Two Cities
import math 

def getPosition(zip): # Function  

	file = open("zips.csv", "r") # opens a file with all US postcodes

	if file.mode == "r": #check if file is opened correctly
		line = file.readline() # read the first line (titles line)

		# declare variables
		zipcode = 0
		city = ""
		latitude = 0
		longtitude = 0
		country = ""


		while line[0] != "": # there is another line in the file
			# filter relevant bits of information
			zipcode = line[1]
			city = line[3]
			latitude = line[6]
			longtitude = line[7]
			country = line[13]

			# if the zipcode is a match return the position object
			if zipcode == zip:
				# print("Zipcode: {}, Country: {}, City: {}, Latitude: {}, Longtitude: {}.".format(zipcode,country,city,latitude,longtitude))
				return Position(latitude,longtitude,city)
			line = file.readline().replace('"','').split(','). # read the next line, remove ' " ' and split by commas



class Position(): # Position object will hold the latitude and longitude for a location

	def __init__(self,latitude,longtitude,location = "unknown"):
		self.latitude = latitude
		self.longtitude = longtitude
		self.location = location



def Distance_between_points(position1, position2): # takes two position objects and access the latitude and longitude

	R = 6371 # radius of the earth in m
	# Using haversine formula to calculate the shortest distance over the earths surface
	# a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)
	# c = 2 ⋅ atan2( √a, √(1−a) )
	# d = R ⋅ c

	pos1_long = float(position1.longtitude)*math.pi/180
	pos1_lat = float(position1.latitude)*math.pi/180

	pos2_long = float(position2.longtitude)*math.pi/180
	pos2_lat = float(position2.latitude)*math.pi/180

	a = math.sin((pos2_lat - pos1_lat)/2)**2 + math.cos(pos1_lat) * math.cos(pos2_lat) * math.sin((pos2_long - pos1_long)/2)**2
	c = 2*math.atan2(math.sqrt(a), math.sqrt(1-a))
	d = R * c

	return d


def main():
	zip1 = string(input('Enter a 5 digit US zip code of the first location: ')) # Ask user for zip codes
	zip2 = string(input('Enter a 5 digit US zip code of the first location: '))

	position1 = getPosition(zip1) # Retrieve the first zip code
	position2 = getPosition(zip2) # Retrieve the second zip code

	distance = Distance_between_points(position1,position2) # call Distance_between_points() to calculate the distance

	print("The distance between {} and {} is: {}".format(position1.location, position2.location, distance)) # display


main()














