from django.db import models
from django import forms

# Create your models here.


class Todo(models.Model):
  """Todo definition."""

  # TODO: Define form fields here
  title = models.CharField( max_length=200)
  due_date = models.DateField(auto_now=False, auto_now_add=False)
  created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True, auto_now_add=False)

  def __str__(self):
      return self.title
  