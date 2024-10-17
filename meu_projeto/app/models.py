from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    # Modificar os campos para evitar conflitos de reverse accessors
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Altere o nome como desejar
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Altere o nome como desejar
        blank=True,
        help_text='Specific permissions for this user.'
    )


class Item(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()

    def __str__(self):
        return self.nome
