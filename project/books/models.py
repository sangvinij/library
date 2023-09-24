from django.db import models


class Reader(models.Model):
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    patronymic = models.CharField(max_length=255, null=False, blank=False)

    objects = models.Manager()

    class Meta:
        constraints = [models.UniqueConstraint(fields=["first_name", "last_name", "patronymic"], name="unique_reader")]

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"


class Book(models.Model):
    STATUS_CHOICES = [("in_stock", "в наличии"), ("on_delivery", "выданы")]

    title = models.CharField(max_length=255, null=False, blank=False)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    status = models.CharField(max_length=11, choices=STATUS_CHOICES, default="in_stock")
    date_deliver = models.DateTimeField(null=True, blank=True)
    date_hand_in = models.DateTimeField(null=True, blank=True)
    reader = models.ForeignKey("reader", on_delete=models.SET_NULL, null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=255, null=False, blank=False)
    last_name = models.CharField(max_length=255, null=False, blank=False)
    patronymic = models.CharField(max_length=255, null=False, blank=False)

    objects = models.Manager()

    class Meta:
        constraints = [models.UniqueConstraint(fields=["first_name", "last_name", "patronymic"], name="unique_author")]

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"
