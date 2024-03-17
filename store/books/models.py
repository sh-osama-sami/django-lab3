from django.db import models
from authors.models import Authors


# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    number_of_pages = models.IntegerField()
    image = models.ImageField(upload_to='books/images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Authors, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def image_url(self):
        return f'/media/{self.image}'

    def create_book(cls, title, price, number_of_pages, image, author):
        try:
            book = cls(title=title, price=price, number_of_pages=number_of_pages, image=image, author=author)
            book.save()
        except Exception as e:
            print(e)
            return None
        return book
