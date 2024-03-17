from django.db import models
from django.shortcuts import get_object_or_404
from django.urls import reverse



# Create your models here.
class Authors(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='authors/images/', blank=True)
    birth_date = models.DateField()


    def __str__(self):
        return self.name

    @property
    def image_url(self):
        return f'/media/{self.image}'

    @property
    def show_url(self):
        url = reverse('authors_detail', args=[self.id])
        return url

    @property
    def edit_url(self):
        url = reverse('authors_update', args=[self.id])
        return url

    @property
    def delete_url(self):
        url = reverse('authors_delete', args=[self.id])
        return url

    @property
    def list_url(self):
        url = reverse('authors_list')
        return url

    @classmethod
    def create_author(cls, name, image, birth_date):
        try:
            author = cls(name=name, image=image, birth_date=birth_date)
            author.save()
        except Exception as e:
            print(e)
            return None
        return author

    @classmethod
    def get_author_by_id(cls, id):
        return get_object_or_404(cls, id=id)

    @classmethod
    def get_all_authors(cls):
        return cls.objects.all()
