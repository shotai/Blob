import blobfinder


class SampleTest:
	def __init__(self, array):
		self.array = array
		self.blob_finder = blobfinder.BlobFinder(self.array)

	def start_test(self):
		self.blob_finder.find_blob()


def main():
	array = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			 [0, 0, 1, 1, 1, 0, 0, 0, 0, 0], \
			 [0, 0, 1, 1, 1, 1, 1, 0, 0, 0], \
			 [0, 0, 1, 0, 0, 0, 1, 0, 0, 0], \
			 [0, 0, 1, 1, 1, 1, 1, 0, 0, 0], \
			 [0, 0, 0, 0, 1, 0, 1, 0, 0, 0], \
			 [0, 0, 0, 0, 1, 0, 1, 0, 0, 0], \
			 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0], \
			 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], \
			 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
	test = SampleTest(array)
	test.start_test()

if __name__ == "__main__":
	main()

