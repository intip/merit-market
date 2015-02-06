from django.db import models

from django.contrib.auth.models import AbstractUser


class Customer(AbstractUser):

    hearts = models.PositiveIntegerField(
        default=0
    )

    weekly_hearts = models.PositiveSmallIntegerField(
        default=15
    )

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return self.full_name


class Transaction(models.Model):

    receiver = models.ForeignKey(
        related_name=''
    )

    giver = models.ForeignKey(
        related_name=''
    )

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

    def __str__(self):
        pass

