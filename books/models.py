from django.db import models

from books.helper import get_integer

# Create your models here.
class Book(models.Model):
  book_id = models.PositiveIntegerField(primary_key=True)
  author = models.CharField(max_length=30)
  title = models.CharField(max_length=50)
  times_read = models.PositiveIntegerField()

  def is_harry_potter(self):
    return self.title.startswith("Harry Potter and the") and self.author == "J.K. Rowling"

  @staticmethod
  def is_by_same_author(book1, book2):
    return book1.author == book2.author


def book_factory(author, title):
  return Book(author=author, title=title)


def is_integer_greater_than_5():
  return True if get_integer() > 5 else False