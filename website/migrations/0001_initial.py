# Generated by Django 2.1.5 on 2019-03-19 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=10)),
                ('days', models.CharField(max_length=200)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('nativeLanguage', models.CharField(max_length=100)),
                ('reading', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reading', to='website.Skills')),
                ('skillLevel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skillLevel', to='website.Skills')),
                ('speaking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='speaking', to='website.Skills')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('languages', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='website.Teacher'),
        ),
        migrations.AddField(
            model_name='student',
            name='vocabulary',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vocabulary', to='website.Skills'),
        ),
        migrations.AddField(
            model_name='course',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Skills'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='website.Teacher'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Course'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Student'),
        ),
    ]
