from django.db import models
import uuid

class ReviewCategory(models.TextChoices):
    MUST = ("Must Watch")
    SHOULD = ("Should Watch")
    AVOID = ("Avoid Watch")
    NO = ("No option")

class Review(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    stars = models.IntegerField()
    review = models.TextField()
    spoilers = models.BooleanField(default=False)
    recomendation = models.CharField(max_length=50, choices=ReviewCategory.choices, default=ReviewCategory.NO)

    # Em relacionamento 1:N utilizamos ForeignKey SEMPRE DO LADO N 
    movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE)
    critic = models.ForeignKey("users.User", on_delete=models.CASCADE)