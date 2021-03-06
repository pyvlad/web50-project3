# Generated by Django 2.0.3 on 2018-05-30 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0003_cart_items_with_extras'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('small', 'Small'), ('large', 'Large')], max_length=10, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SelectedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menuitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.MenuItem')),
            ],
        ),
        migrations.CreateModel(
            name='Selection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.ManyToManyField(through='orders.SelectedItem', to='orders.MenuItem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='products',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='user',
        ),
        migrations.RemoveField(
            model_name='cartproduct',
            name='cartitem',
        ),
        migrations.RemoveField(
            model_name='cartproduct',
            name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
        migrations.DeleteModel(
            name='CartProduct',
        ),
        migrations.DeleteModel(
            name='ProductSize',
        ),
        migrations.AddField(
            model_name='selecteditem',
            name='selectedproduct',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Selection'),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='orders.Product'),
        ),
    ]
