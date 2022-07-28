from django.db import models
import uuid

class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10)
    premiere = models.DateField()
    classification = models.IntegerField()
    synopsis = models.TextField()

    genres = models.ManyToManyField("genres.Genre", related_name="movies")