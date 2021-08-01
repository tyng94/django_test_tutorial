import pytest

import books.helper
from books import helper
from books.models import Book

class TestMockConstant:
  def test_get_integer(self):
    assert helper.get_integer() == 2

  def test_get_integer_1(self, mocker):
    mocker.patch("books.helper.CONSTANT_INTEGER", 3)
    assert helper.get_integer() == 3

  # #Negative example - Do not modify constant directly!
  # #Uncomment to see what happens
  # def test_foo_2(self):
  #   mock_constant = 3
  #   helper.CONSTANT_INTEGER = mock_constant
  #   assert helper.is_integer_greater_than_3() == 3
  #
  # def test_foo(self):
  #   assert helper.get_integer() == 2


class TestMockFunction:
  def test_is_integer_greater_than_3(self):
    assert helper.is_integer_greater_than_3() == False

  def test_is_integer_greater_than_3_1(self, mocker):
    mocker.patch("books.helper.get_integer").return_value = 4
    assert helper.is_integer_greater_than_3() == True

  # def test_is_integer_greater_than_3_is_called(self, mocker):
  #   mocker.patch("books.helper.get_integer").return_value = 4
  #   spy = mocker.spy(books.helper, "get_integer")
  #   assert helper.is_integer_greater_than_3() == True
  #   assert spy.call_count == 1
  #
  # def test_is_integer_greater_than_3_is_called_2(self, mocker):
  #   mocker.patch("books.helper.get_integer").return_value = 4
  #   assert helper.is_integer_greater_than_3() == True
  #   assert books.helper.get_integer.assert_called_once_with()


class TestMockClassMethod:
  def test_is_harry_potter(self):
    book = Book(
      author="J.K. Rowling",
      title="Harry Potter and the Prisoner of Askaban",
      times_read=3
    )
    assert book.is_harry_potter() == True

  def test_is_harry_potter_1(self, mocker):
    book = Book(
      author="J.K. Rowling",
      title="Harry Potter and the Prisoner of Askaban",
      times_read=3
    )
    mocker.patch("books.models.Book.is_harry_potter").return_value = False
    assert book.is_harry_potter() == False

  def test_is_harry_potter_alternative(self, mocker):
    book = mocker.Mock()
    book.is_harry_potter.return_value = False
    assert book.is_harry_potter() == False
