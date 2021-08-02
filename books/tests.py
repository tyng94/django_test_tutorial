from books import helper
from books.models import Book, is_integer_greater_than_5, book_factory

# Create your tests here.
class TestMockConstant:
  # # Negative example - Do not modify constant directly!
  # # Uncomment to see what happens
  # def test_get_integer_bad(self):
  #   helper.CONSTANT_INTEGER = 3
  #   assert helper.get_integer() == 3

  def test_get_integer_without_mock(self):
    assert helper.get_integer() == 2

  def test_get_integer_with_mock(self, mocker):
    mocker.patch("books.helper.CONSTANT_INTEGER", 3)
    assert helper.get_integer() == 3


class TestMockFunction:
  def test_is_integer_greater_than_3_without_mock(self):
    assert helper.is_integer_greater_than_3() == False

  def test_is_integer_greater_than_3_with_mock(self, mocker):
    mocker.patch("books.helper.get_integer").return_value = 4
    assert helper.is_integer_greater_than_3() == True

  def test_is_integer_greater_than_5_without_mock(self):
    assert is_integer_greater_than_5() == False

  def test_is_integer_greater_than_5_with_mock(self, mocker):
    mocker.patch("books.models.get_integer").return_value = 6
    assert is_integer_greater_than_5() == True

  # def test_is_integer_greater_than_3_is_called(self, mocker):
  #   mocker.patch("books.get_integer").return_value = 4
  #   spy = mocker.spy(books. "get_integer")
  #   assert is_integer_greater_than_3() == True
  #   assert spy.call_count == 1
  #
  # def test_is_integer_greater_than_3_is_called_2(self, mocker):
  #   mocker.patch("books.get_integer").return_value = 4
  #   assert is_integer_greater_than_3() == True
  #   assert books.get_integer.assert_called_once_with()


class TestMockClassMethod:
  def test_is_harry_potter_without_mock(self):
    book = Book(
      author="J.K. Rowling",
      title="Harry Potter and the Prisoner of Askaban",
      times_read=3
    )
    assert book.is_harry_potter() == True

  def test_is_harry_potter_with_mock(self, mocker):
    book = Book(
      author="J.K. Rowling",
      title="Harry Potter and the Prisoner of Askaban",
      times_read=3
    )
    mocker.patch("books.models.Book.is_harry_potter").return_value = False
    assert book.is_harry_potter() == False

  def test_is_harry_potter_mock_object_method(self, mocker):
    book = mocker.Mock()
    book.is_harry_potter.return_value = False
    assert book.is_harry_potter() == False

class TestMockStaticMethod:
  def test_is_same_author_without_mock(self):
    book1 = Book(
      author="J.K. Rowling",
      title="Harry Potter and the Prisoner of Askaban",
      times_read=3
    )
    book2 = Book(
      author="J.R.R Tolkien",
      title="The Hobbit",
      times_read=2
    )
    assert not Book.is_by_same_author(book1, book2)

  def test_is_same_author_with_mock(self, mocker):
    book1 = Book(
      author="J.K. Rowling",
      title="Harry Potter and the Prisoner of Askaban",
      times_read=3
    )
    book2 = Book(
      author="J.R.R Tolkien",
      title="The Hobbit",
      times_read=2
    )
    mocker.patch("books.models.Book.is_by_same_author").return_value = True
    assert Book.is_by_same_author(book1, book2)

  def test_is_same_author_mock_object_variables(self, mocker):
    book1 = mocker.Mock()
    book1.author = "J.R.R Tolkien"
    book1.title = "The Hobbit"

    book2 = Book(
      author="J.R.R Tolkien",
      title="The Hobbit",
      times_read=2
    )
    assert Book.is_by_same_author(book1, book2)


class TestMockClass:
  def test_book_factory(self, mocker):
    book = book_factory("J.K. Rowling", "Harry Potter and the Prisoner of Askaban")
    assert book.title == "Harry Potter and the Prisoner of Askaban"
    assert book.author == "J.K. Rowling"

  def test_book_factory_mock_class(self, mocker):
    returned_book = mocker.patch("books.models.Book").return_value
    returned_book.author = "J.R.R Tolkien"
    returned_book.title = "The Hobbit"

    book = book_factory("J.K. Rowling", "Harry Potter and the Prisoner of Askaban")
    assert book.title == "The Hobbit"
    assert book.author == "J.R.R Tolkien"