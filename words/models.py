from django.db import models
from django_userforeignkey.models.fields import UserForeignKey


class Country(models.Model):
    name = models.CharField(max_length = 60)
    alpha_2 = models.CharField(max_length=2)
    alpha_3 = models.CharField(max_length=3)
    country_code = models.IntegerField()
    region = models.CharField(max_length=15)
    sub_region = models.CharField(max_length=30)
    region_code = models.IntegerField()
    sub_region_code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Language(models.Model):
    language_name = models.CharField(max_length=50)
    alpha_2 = models.CharField(max_length=2)
    alpha_3 = models.CharField(max_length=3)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.language_name

class Word(models.Model):
    text = models.CharField(max_length = 50)
    original_language_code = models.ForeignKey(Language,related_name='original',on_delete=models.CASCADE)
    translation_text = models.CharField(max_length = 50)
    translation_language_code = models.ForeignKey(Language,related_name='translation',on_delete=models.CASCADE)
    full_original_sentence = models.TextField()
    user = user = UserForeignKey(auto_user_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

