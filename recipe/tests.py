from django.test import TestCase
from django.urls import reverse
from .models import Recipe

class RecipeViewsTestCase(TestCase):
    def setUp(self):
        self.recipe = Recipe.objects.create(
            name='Test Recipe',
            description='Test Description',
            ingredients='Test Ingredients',
            instructions='Test Instructions',
            date='2023-01-01'
        )

    def test_main_view(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Recipe')

    def test_recipe_detail_view(self):
        response = self.client.get(reverse('recipe_detail', args=[self.recipe.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Recipe')
        self.assertContains(response, 'Test Description')
