from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
	user = models.OneToOneField(User)
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)

	def __unicode__(self):
		self.user.username
		


class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	likes = models.IntegerField(default=0)
	slug = models.SlugField()

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)

		super(Category, self).save(*args, **kwargs)


	def __unicode__(self):  #For Python 2, use __str__ on Python 3
		return self.name



class Page(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)

	def __unicode__(self):      #For Python 2, use __str__ on Python 3
		return self.title

