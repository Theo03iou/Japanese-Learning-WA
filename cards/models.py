from django.db import models

# Create your models here.

class Card(models.Model):
    jp_word = models.CharField(max_length=20)
    en_word = models.CharField(max_length=30)
    jp_sentence = models.CharField(max_length=100)
    en_sentence = models.CharField(max_length=100)
    card_img = models.ImageField(upload_to="images", null=True)
    card_audio = models.FileField(upload_to='audio', null=True)   
    review_date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)