from django.db import models
from django.contrib.auth.models import User


class Customer(User):

    hearts = models.PositiveIntegerField(
        default=0
    )

    weekly_hearts = models.PositiveSmallIntegerField(
        default=15
    )

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"


class Transaction(models.Model):

    receiver = models.ForeignKey(
        Customer,
        related_name='received'
    )

    giver = models.ForeignKey(
        Customer,
        related_name='given'
    )

    qtty = models.PositiveSmallIntegerField(
        default=1
    )

    transaction_time = models.DateTimeField(
        auto_now_add=True
    )

    comment = models.CharField(
        max_length=140,
    )

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "Transactions"

    def save(self, *args, **kwargs):
        """
            Metodo que gerencia a transferencia de transacao
        """
        if self.receiver == self.giver:
            raise ValueError('Receive most be different from giver')
        elif self.giver.weekly_hearts < self.qtty:
            raise ValueError('Not weekly hearts or qty more available')

        self.giver.weekly_hearts -= self.qtty
        self.giver.save()
        self.receiver.hearts += self.qtty
        self.receiver.save()

        return super(Transaction, self).save(*args, **kwargs)

    def __str__(self):
        return "{0} to {1} - {2} hearts".format(
               self.giver,
               self.receiver,
               self.qtty)
