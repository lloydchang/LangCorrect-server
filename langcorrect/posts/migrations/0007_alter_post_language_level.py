# Generated by Django 4.2.7 on 2024-01-08 00:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0006_alter_post_is_corrected"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="language_level",
            field=models.CharField(
                choices=[
                    ("A1", "Beginner"),
                    ("A2", "Elementary"),
                    ("B1", "Intermediate"),
                    ("B2", "Upper-Intermediate"),
                    ("C1", "Advanced"),
                    ("C2", "Proficient"),
                    ("N", "Native"),
                ],
                default="A1",
                max_length=2,
            ),
        ),
    ]
