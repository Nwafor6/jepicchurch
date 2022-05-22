from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# from django.temp

# Create your models here.

class Upcoming_Event(models.Model):
	title= models.CharField(max_length=200)
	program_content=models.TextField()
	slug=models.SlugField(unique=True, max_length=255)
	image=models.ImageField(upload_to='events-images', blank=True, null=True)
	program_date=models.DateTimeField()
	pub_date=models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural= "Upcoming Events"

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug=slugify(self.title)
		super(Upcoming_Event, self).save(*args, **kwargs)


class Gallery(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	title=models.CharField(max_length=250)
	page_image=models.ImageField(null=True, blank=True, help_text='Use puns liberally',)
	slug=models.SlugField(unique=True, max_length=255)

	def __str__(self):
		return f"{self.title} image Gallery"

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug=slugify(self.title)
		super(Gallery, self).save(*args, **kwargs)

	@property
	def images(self):
		"""return all list of all uploaded images"""
		return self.galleryimage_set.all() 

class GalleryImage(models.Model):
	gallery=models.ForeignKey(Gallery, on_delete=models.CASCADE, null=True)
	image=models.ImageField(null=True, blank=True)
	

	def __str__(self):
		return f"{self.gallery.title} {self.pk}"

	@property
	def image_url(self):
		return get_image_url(self, 'image')


