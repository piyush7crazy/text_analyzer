from django.db import models

class Analyzer(models.Model):
    text=models.TextField()
    word_count=models.IntegerField()
    character_count=models.IntegerField()
    sentence_count=models.IntegerField()
    word_frequencies=models.TextField()
    readability_score=models.DecimalField(max_digits=12 , decimal_places=2)
