from django.contrib import admin

# Register your models here.

from .models import CardTemplate, DeckTemplate, UserDeck, UserCard

admin.site.register(CardTemplate)
admin.site.register(DeckTemplate)
admin.site.register(UserDeck)
admin.site.register(UserCard)