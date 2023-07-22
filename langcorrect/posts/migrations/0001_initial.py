# Generated by Django 4.2.3 on 2023-07-21 02:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import taggit.managers


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("languages", "0001_initial"),
        ("taggit", "0005_auto_20220424_2025"),
        ("prompts", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="modified"
                    ),
                ),
                ("is_removed", models.BooleanField(default=False)),
                ("title", models.CharField(max_length=60)),
                ("text", models.TextField()),
                ("native_text", models.TextField()),
                (
                    "gender_of_narration",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("O", "Other"), ("U", "Prefer not to say")],
                        default="U",
                        max_length=1,
                    ),
                ),
                (
                    "permission",
                    models.CharField(
                        choices=[
                            ("public", "Viewable by everyone"),
                            ("member", "Viewable only by registered members"),
                        ],
                        default="public",
                        max_length=6,
                    ),
                ),
                ("is_draft", models.BooleanField(default=False)),
                ("slug", models.SlugField(max_length=255, null=True)),
                ("language_level", models.CharField(blank=True, max_length=30, null=True)),
                ("is_corrected", models.IntegerField(default=0)),
                ("language", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="languages.language")),
                (
                    "prompt",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="prompts.prompt"
                    ),
                ),
                (
                    "tags",
                    taggit.managers.TaggableManager(
                        blank=True,
                        help_text="A comma-separated list of tags.",
                        through="taggit.TaggedItem",
                        to="taggit.Tag",
                        verbose_name="Tags",
                    ),
                ),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "ordering": ["-created"],
            },
        ),
    ]