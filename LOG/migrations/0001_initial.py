# Generated by Django 4.1.3 on 2023-01-15 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='classes',
            fields=[
                ('Semester', models.CharField(max_length=5)),
                ('Section', models.CharField(max_length=2, verbose_name='Section')),
                ('department', models.CharField(max_length=20)),
                ('Class_Code', models.CharField(max_length=25, primary_key=True, serialize=False)),
                ('OOPS_lab', models.CharField(max_length=20)),
                ('DS_lab', models.CharField(max_length=20)),
                ('DBMS_lab', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Labs',
            fields=[
                ('LAB_CODE', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Course_name', models.CharField(max_length=30)),
                ('faculty_name', models.CharField(max_length=30)),
                ('credits', models.IntegerField()),
                ('Hours_per_week', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('Name', models.CharField(max_length=25, verbose_name='Student name')),
                ('Department', models.CharField(max_length=25, verbose_name='department name')),
                ('Semester', models.CharField(max_length=5)),
                ('Section', models.CharField(max_length=2, verbose_name='Section')),
                ('Contact_no', models.CharField(max_length=11)),
                ('USN', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OOPS_lab', models.CharField(max_length=20)),
                ('DS_lab', models.CharField(max_length=20)),
                ('DBMS_lab', models.CharField(max_length=20)),
                ('Class_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LOG.classes')),
                ('USN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LOG.student')),
            ],
        ),
    ]
