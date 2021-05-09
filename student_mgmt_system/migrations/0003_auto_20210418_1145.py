# Generated by Django 3.1.7 on 2021-04-18 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_mgmt_system', '0002_auto_20210411_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='stream',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='student_mgmt_system.stream'),
        ),
    ]