# Generated by Django 2.1.4 on 2021-06-10 06:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webservices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.BooleanField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'project_students',
            },
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.BooleanField(default=1)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'project_subjects',
            },
        ),
        migrations.AlterField(
            model_name='marks',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='webservices.Students'),
        ),
        migrations.AlterField(
            model_name='marks',
            name='subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='webservices.Subjects'),
        ),
    ]
