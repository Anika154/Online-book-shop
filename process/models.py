from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.body


class Book(models.Model):
    book_id = models.IntegerField()
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    amount = models.IntegerField()
    price = models.IntegerField()

    def __int__(self):
        return self.book_id


class Order(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.customer.name + "--" + self.book.name
