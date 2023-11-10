from django.db import models


# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    class Meta:
        db_table = "employee"

    def to_dict(self):
        return {

            'name': self.name,
            'email': self.email
        }
