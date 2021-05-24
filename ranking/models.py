from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here.
class RankingCard(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, null=True, related_name='ranking_card', on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	description = models.TextField(blank=False)

	class Meta:
		db_table = "ranking_card"

	def __str__(self):
		return '%s' % (self.name)
