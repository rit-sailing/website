from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify
from main.models import TeamMember
from django.db import models
import re

class Folder(models.Model):
	name = models.CharField(max_length=20)
	parent = models.ForeignKey('self', default=None, null=True, blank=True)
	slug = models.SlugField()
	def __str__(self):
		return self.name
	def validate_unique(self, *args, **kwargs):
		super(Folder, self).validate_unique(*args, **kwargs)
		for item in self.__class__.objects.filter(parent=self.parent):
			if item.pk != self.pk and item.name == self.name:
				raise ValidationError()
	def save(self):
		self.slug = slugify(self.name)
		super(Folder, self).save()

def file_path(instance, filename):
	path = "/"
	current = instance.parent
	while(current != None):
		path = "/" + current.slug + path
		current = current.parent
	return 'files' + path + filename

class File(models.Model):
	name = models.CharField(max_length=20)
	content = models.FileField(upload_to=file_path)
	description = models.CharField(max_length=100, blank=True)
	publish_date = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	uploaded_by = models.ForeignKey(TeamMember)
	parent = models.ForeignKey(Folder, null=True, blank=True)
	slug = models.SlugField()
	def get_path(self):
		path = "/"
		current = self.parent
		while(current != None):
			path += current.name + "/"
			current = current.parent
		return path
	def __str__(self):
		return self.name
	def save(self):
	   self.slug = slugify(self.name)
	   super(File, self).save()
