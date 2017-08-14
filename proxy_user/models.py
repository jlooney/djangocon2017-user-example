from django.db import models
from django.contrib.auth.models import User


class Author(User):

    class Meta:
        proxy = True

    def __str__(self):
        return self.first_name
