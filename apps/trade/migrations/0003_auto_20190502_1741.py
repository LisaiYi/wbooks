# Generated by Django 2.0.5 on 2019-05-02 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0002_auto_20190501_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='post_script',
            field=models.CharField(default='用户未添加留言', max_length=200, verbose_name='订单留言'),
        ),
    ]
