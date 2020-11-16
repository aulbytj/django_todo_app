from django.db import models

# Create your models here.

LABEL_CHOICES = (
  ('primary','In Progress'),
  ('secondary','Pending'),
  ('success','Completed'),
)

class Todo(models.Model):
  """Todo definition."""

  # TODO: Define form fields here
  title = models.CharField( max_length=200)
  due_date = models.DateField(auto_now=False, auto_now_add=False)
  label = models.CharField(choices=LABEL_CHOICES, max_length=20, default='Pending')
  completed = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
  update_at = models.DateTimeField(auto_now=True, auto_now_add=False)

  def __str__(self):
      return self.title
  