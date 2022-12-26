from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100,
                            help_text="Enter menu name",
                            null=False,
                            unique=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               related_name='child',
                               blank=True,
                               null=True)

    def __str__(self):
        return self.name
