# Generated by Django 3.0.6 on 2020-05-09 22:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0005_auto_20200509_1936'),
        ('documentos', '0002_documento_belong'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='belong',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='funcionarios.Funcionario'),
        ),
    ]