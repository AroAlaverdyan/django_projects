from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

STATUS_CHOICES_N = (
	(0, "Allow"),
	(1, "Don't Allow"),
	)

STATUS_CHOICES_S = (
	(0, "New"),
	(1, "Doing"),
	(2, "Done"),
	)

class NewToDo(models.Model):
	name = models.CharField(max_length = 15)
	description = models.TextField()
	date_time = models.DateTimeField(default = timezone.now)
	notification = models.IntegerField(choices = STATUS_CHOICES_N, default = "0")
	status = models.IntegerField(choices = STATUS_CHOICES_S)
	user = models.ForeignKey(User, on_delete = models.CASCADE, default = 1)

	def __str__(self):
		return self.name
