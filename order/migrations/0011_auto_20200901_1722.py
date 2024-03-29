# Generated by Django 3.0.5 on 2020-09-01 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_auto_20200830_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.SmallIntegerField(choices=[(1, '待付款'), (3, '待评价'), (4, '已完成'), (2, '待交易')], default=2, verbose_name='订单状态'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pay_method',
            field=models.SmallIntegerField(choices=[(3, '支付宝'), (2, '微信支付'), (1, '当面付款')], default=1, verbose_name='支付方式'),
        ),
    ]
