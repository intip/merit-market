# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('hearts', models.PositiveIntegerField(default=0)),
                ('weekly_hearts', models.PositiveSmallIntegerField(default=15)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qtty', models.PositiveSmallIntegerField(default=1)),
                ('transaction_time', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(max_length=140)),
                ('giver', models.ForeignKey(related_name='given', to='core.Customer')),
                ('receiver', models.ForeignKey(related_name='received', to='core.Customer')),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
            },
            bases=(models.Model,),
        ),
    ]
