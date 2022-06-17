from locale import currency
from django.db import models


class Deposit(models.Model):
    amount_money = models.IntegerField(
        null=False,
        blank=False,
        verbose_name="amount_of_money",        
    )

    
