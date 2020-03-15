# import uuid
# from idlelib.multicall import r
from django.db import models
from django_mysql.models import JSONField


class Superhero(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    squad_name = models.CharField(max_length=100)
    hometown = models.CharField(max_length=30)
    formed = models.DateField()
    active = models.BooleanField()
    members = JSONField()

    class Meta:
        db_table = "superheros"
        ordering = ['id']

    def __str__(self):
        return "id {}, squad_name {} hometown {} formed {} active {} members {}".format(self.id, self.squad_name,
                                                                                        self.hometown, self.formed, self.active, self.members)
    

#