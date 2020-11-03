import requests


class req_1:
	def __init__(self, url):
		self.response = requests.get(url)

	def download(self):
		with open("image.jpeg","wb") as f:
			f.write(self.response.content)

class req_2:
	def download(self, response):
		with open("image.png","wb") as f:
			f.write(response.content)


class Polimorf(req_1, req_2):
	def __init__(self, url):
		req_1.__init__(self, url)

	def download(self):
		if c.lower() == "jpeg":
			req_1.download(self)
		else:
			req_2.download(self, self.response)


object_1 = Polimorf("http://www.httpbin.org/image/jpeg")
object_1.download()
