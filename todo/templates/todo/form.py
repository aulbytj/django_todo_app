from django import forms
from . models import Todo

class TodoForm(forms.ModelForm):
  """Form definition for Todo."""

  class Meta:
    """Meta definition for Todoform."""

    model = Todo
    fields = (
      'title', 
      'due_date',
      'created_at',
      'updated_at',
      )
