from rest_framework import serializers
from .models import Analyzer

class AnalyzerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Analyzer
        fields=['text', 'word_count' , 'character_count' , 'sentence_count' , 'word_frequencies' , 'readability_score' , 'id']
        read_only_fields=['word_count' , 'character_count' , 'sentence_count' , 'word_frequencies' , 'readability_score' , 'id']