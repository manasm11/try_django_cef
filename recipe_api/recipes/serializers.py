from rest_framework import serializers
from .models import Recipe, Ingredient, Upvote
from django.db.models import Sum

class RecipeSerializer(serializers.ModelSerializer):
    total_calories = serializers.SerializerMethodField()

    def get_total_calories(self, recipe):
        return Ingredient.objects.filter(recipe=recipe).aggregate(Sum('calories'))
    class Meta:
        model = Recipe
        fields = [
            'id',
            'author',
            'title',
            'image',
            'time_mins',
            'ingredients',
            'diet',
            'created',
            'updated',
            'total_calories',
        ]
        read_only_fields = ['id', 'author']