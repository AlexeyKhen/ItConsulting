from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()

Categories = [
    ('1st', 'Первая'),
    ('2nd', 'Вторая'),
    ('3rd', 'Третья'),

]


def upload_post_image(instance, filename):
    return f'{instance.author}/{filename}'


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to=upload_post_image)
    category = models.CharField(max_length=3, choices=Categories)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detailview', args=[str(self.pk)])
