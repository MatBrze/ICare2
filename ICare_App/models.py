from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Organisation(models.Model):
    name = models.CharField(max_length=50)
    required_items = models.ForeignKey(Item, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    target = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} {self.location}'


class Donation(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    post_code = models.CharField(max_length=6)
    phone_number = models.CharField(max_length=12)
    date = models.DateField()
    time = models.TimeField()
    remarks = models.TextField(max_length=500)

    def __str__(self):
        return f'[{self.date}] - {self.item} for {self.organisation}'


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
