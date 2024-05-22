from django.db import models
from django.conf import settings

# Create your models here.

class CardTemplate(models.Model):
    jp_word = models.CharField(max_length=20)
    en_word = models.CharField(max_length=30)
    jp_sentence = models.CharField(max_length=100)
    en_sentence = models.CharField(max_length=100)
    card_img = models.ImageField(upload_to="images", null=True)
    card_audio = models.FileField(upload_to='audio', null=True)   
    review_date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    
class DeckTemplate(models.Model):
    name = models.CharField(max_length=50)
    cards = models.ManyToManyField(CardTemplate)
    
    def __str__(self):
        return self.name
    
    
class UserDeck(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="decks")
    template = models.ForeignKey(DeckTemplate, on_delete=models.PROTECT)
    customised_cards = models.ManyToManyField(CardTemplate, through="UserCard", related_name="user_decks")
    
    def __str__(self):
        return f"{self.user.username}'s deck"
    
class UserCard(models.Model):
    user_deck = models.ForeignKey(UserDeck, on_delete=models.CASCADE)
    card_template = models.ForeignKey(CardTemplate, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    
    # LATER PUT IN THINGS LIKE REVIEW DATE, NUMBER OF TIMES SEEN
    
    def __str__(self):
        return f"{self.card_template.jp_word} in {self.user_deck.template.name}"