from django.db import models
from django.contrib.postgres.fields import JSONField


class Category(models.Model):
    """
    Category model stored all categories with parent category.
    """
    name = models.CharField(max_length=250)
    description = models.TextField(help_text="Category description", null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """
        Stringify return model object.
        :return: It return category name.
        """
        return "{}".format(self.name)


class SubCategory(models.Model):
    """
    Category model stored all categories with parent category.
    """
    category = models.ForeignKey(Category, null=True, blank=True, related_name="main_category")
    name = models.CharField(max_length=250)
    description = models.TextField(help_text="Category description", null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """
        Stringify return model object.
        :return: It return sub-category name.
        """
        return "{}".format(self.name)


class Product(models.Model):
    """
    Product model stores product information with categories
    """
    title = models.CharField(max_length=220, default="Default product")
    description = models.TextField(blank=True, null=True)
    sub_category = models.ForeignKey("SubCategory", null=True, blank=True)
    technical_specification = JSONField(blank=True, null=True)
    product_type = models.CharField(max_length=220, null=True)
    cost = models.IntegerField(default=10)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """
        Stringify return model object.
        :return: It return product name.
        """
        return "{}".format(self.title)
