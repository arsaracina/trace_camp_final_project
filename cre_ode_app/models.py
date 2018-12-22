from django.db import models

# Create your models hereself.
class DiffEq(models.Model):
    lhs = models.TextField()
    rhs = models.IntegerField()
    parameter = models.IntegerField()
    init_cond = models.IntegerField()
    test_range = models.IntegerField()
