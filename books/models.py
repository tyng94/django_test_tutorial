from django.db import models

# Create your models here.
class Book(models.Model):
  book_id = models.PositiveIntegerField(primary_key=True)
  author = models.CharField(max_length=30)
  title = models.CharField(max_length=50)
  times_read = models.PositiveIntegerField()

  def is_harry_potter(self):
    return self.title.startswith("Harry Potter and the") and self.author == "J.K. Rowling"

