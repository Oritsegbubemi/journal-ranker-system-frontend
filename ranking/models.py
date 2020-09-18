from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here.
class Card(models.Model):
	user = models.ForeignKey(User, null=True, related_name="ranking_card", on_delete=models.CASCADE)
	#card_name
	name = models.CharField(max_length=100)
	#card_description
	description = models.TextField(blank=True)

	def __str__(self):
		return '%s' % (self.name)
