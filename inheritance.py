class Make:
	def __init__(self, name):
		self.name = name

class Automobile(MotorizedVehicle):
	def __init__(self, year, make, model):
		self.year = year
		self.make = make
		self.model = model
		
		self.tires = []
	
	def drive():
		pass
	
	def get_make(self):
		return self.make
	
	def __repr__(self):
		return str(self.year) + " " + self.make + " " + self.model
	
	def __str__(self):
		return self.__repr__()

class Sedan(Automobile):
	def __init__(self, year, make, model):
		super().__init__(year, make, model)
	
	def drive():
		pass

my_sedan.drive()

class Pickup(Automobile):
	def __init__(self, year, make, model, bed_width, bed_length):
		super().__init__(year, make, model)
		
		self.bed_width = bed_width
		self.bed_length = bed_length
	
	def get_bed_area(self):
		return self.bed_width * self.bed_length

class JSONSerializable:
	def from_JSON():
		pass
	
	def to_JSON():
		pass

class XMLSerizalizable;
	