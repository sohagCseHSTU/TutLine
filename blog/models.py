from django.db import models

class blog(models.Model):
	title = models.CharField(max_length=10)
	text = models.TextField()
	published_time = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title
