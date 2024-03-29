# Generated by Django 5.0.3 on 2024-03-09 11:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("academic", "0001_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="section",
            name="teacher",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="users.teacher",
            ),
        ),
        migrations.AddField(
            model_name="assignment",
            name="section",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="academic.section"
            ),
        ),
        migrations.AddField(
            model_name="standard",
            name="teacher",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="users.teacher",
            ),
        ),
        migrations.AddField(
            model_name="section",
            name="standard",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="academic.standard"
            ),
        ),
        migrations.AddField(
            model_name="assignment",
            name="standard",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="academic.standard"
            ),
        ),
        migrations.AddField(
            model_name="subject",
            name="teacher",
            field=models.ManyToManyField(to="users.teacher"),
        ),
        migrations.AddField(
            model_name="standard",
            name="subject",
            field=models.ManyToManyField(to="academic.subject"),
        ),
        migrations.AddField(
            model_name="assignment",
            name="subject",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="academic.subject"
            ),
        ),
        migrations.AddField(
            model_name="syllabus",
            name="standard",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="academic.standard"
            ),
        ),
        migrations.AddField(
            model_name="syllabus",
            name="subject",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="academic.subject"
            ),
        ),
    ]
