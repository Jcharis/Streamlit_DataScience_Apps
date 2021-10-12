from locust import HttpUser,task,between 

class AppUser(HttpUser):
	wait_time = between(2,5)

	# Endpoint
	@task
	def home_page(self):
		self.client.get("/")



# Code to run
# locust -f locust_file.py --host http://localhost:8501 --users 200