class BlobFinder:
	def __init__(self, input_array):
		self.input_array = input_array
		self.visited_dict = {}
		self.edges = {'top': 10, 'left': 10, 'bottom': 0, 'right': 0}
		self.read_cells = 0

	def find_blob(self):
		if not self.process_data():
			return
		self.start_search()
		self.print_results()

	def process_data(self):
		# generate the initial visited_dict
		r, c = len(self.input_array),  len(self.input_array[0])
		if r > 10 or c > 10:
			print("out of boundary, the input should be 10*10 array")
			return False
		for i in range(r):
			for j in range(c):
				self.visited_dict[(i,j)] = [self.input_array[i][j], False]
		return True

	def start_search(self):
		# find the occupied node
		for vec in self.visited_dict:
			if self.visited_dict[vec][0] == 1:
				self.search_neighbours(vec)

	def search_neighbours(self, vec):
		# search the unvisited neighbours to find the occupied one
		self.read_cells += 1
		if self.check_node_status((vec[0]-1, vec[1])):  # Up
			self.search_neighbours((vec[0]-1, vec[1]))
		if self.check_node_status((vec[0],vec[1]-1)):   # Left
			self.search_neighbours((vec[0], vec[1]-1))
		if self.check_node_status((vec[0]+1, vec[1])):  # Down
			self.search_neighbours((vec[0]+1,vec[1]))
		if self.check_node_status((vec[0], vec[1]+1)):  # Right
			self.search_neighbours((vec[0], vec[1]+1))

		self.update_edge(vec)

	def update_edge(self, vec):
		# update the blob's edge
		if self.edges['top'] > vec[0]:     # Up
			self.edges['top'] = vec[0]
		if self.edges['left'] > vec[1]:    # Left
			self.edges['left'] = vec[1]
		if self.edges['bottom'] < vec[0]:  # Down
			self.edges['bottom'] = vec[0]
		if self.edges['right'] < vec[1]:   # Right
			self.edges['right'] = vec[1]


	def check_node_status(self, key):
		# check if the node is visited and occupied
		status = False
		try:
			if self.visited_dict[key] == [1, False]:
				status = True
				self.visited_dict[key][1] = True
		except: # meet the edge of the input array
			return False
		return status

	def print_results(self):
		# print the output
		print('Cell Reads: %s' % self.read_cells)
		print("Top: %s" % self.edges['top'])
		print("Left: %s" % self.edges['left'])
		print("Bottom: %s" % self.edges['bottom'])
		print("Right: %s" % self.edges['right'])

	def get_location(self):
		# get the boundaries
		return self.edges

	def get_read_count(self):
		# get the read cells count
		return self.read_cells



