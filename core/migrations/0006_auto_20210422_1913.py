# Generated by Django 3.1.7 on 2021-04-22 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20210422_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='organization',
            name='contact',
            field=models.ManyToManyField(blank=True, to='core.Contact'),
        ),
        migrations.AlterField(
            model_name='program',
            name='affiliations',
            field=models.ManyToManyField(blank=True, to='core.Organization'),
        ),
        migrations.AlterField(
            model_name='program',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='program',
            name='contact',
            field=models.ManyToManyField(blank=True, to='core.Contact'),
        ),
        migrations.AlterField(
            model_name='program',
            name='focus',
            field=models.ManyToManyField(blank=True, to='core.Tag'),
        ),
        migrations.AlterField(
            model_name='program',
            name='technology_tags',
            field=models.ManyToManyField(blank=True, to='core.Technology_Tag'),
        ),
    ]
