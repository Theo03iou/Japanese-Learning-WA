# Generated by Django 5.0.1 on 2024-05-22 19:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DeckTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cards', models.ManyToManyField(to='cards.cardtemplate')),
            ],
        ),
        migrations.CreateModel(
            name='UserCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('card_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.cardtemplate')),
            ],
        ),
        migrations.RenameModel(
            old_name='Card',
            new_name='CardTemplate',
        ),
        migrations.CreateModel(
            name='UserDeck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customised_cards', models.ManyToManyField(related_name='user_decks', through='cards.UserCard', to='cards.cardtemplate')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cards.decktemplate')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='decks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='usercard',
            name='user_deck',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards.userdeck'),
        ),
    ]