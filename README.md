# djangocon2017-user-example
Notes for my Djangocon 2017 talk 'Getting the Most out of Django's User Model.'

My talk covered three main options for customizing the user model.

1. Proxy Model
2. 1-1 relationship model
3. Custom user model

You will notice that there are directories for the first two options. These contain small code snippets that were featured in my presentation. Most information you will need you can find on Django's documentation. Below you can find links to relevant docs for each option.

## 1. Proxy model

- On proxy models in general: https://docs.djangoproject.com/en/1.11/topics/db/models/#proxy-models

## 2. 1-1 Relationship with the User Model

- On Django's OneToOneField in general: https://docs.djangoproject.com/en/1.11/ref/models/fields/#onetoonefield
- On setting up a 1-1 relationship with the user model (as well as the django admin): https://docs.djangoproject.com/en/1.11/topics/auth/customizing/#extending-the-existing-user-model
- On post_save signals: https://docs.djangoproject.com/en/1.11/ref/signals/#post-save

## 3. Custom User model

- On custom user models in general: https://docs.djangoproject.com/en/1.11/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
- On setting up a custom user model: https://docs.djangoproject.com/en/1.11/topics/auth/customizing/#specifying-a-custom-user-model
- On AbstractBaseUser: https://docs.djangoproject.com/en/1.11/topics/auth/customizing/#django.contrib.auth.models.AbstractBaseUser
- A fully implemented example of a custom user model: https://docs.djangoproject.com/en/1.11/topics/auth/customizing/#a-full-example 
