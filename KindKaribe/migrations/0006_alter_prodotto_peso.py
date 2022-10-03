# Generated by Django 4.1.1 on 2022-10-03 18:27

import KindKaribe.models
from django.db import migrations
import enumchoicefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ("KindKaribe", "0005_alter_prodotto_peso"),
    ]

    operations = [
        migrations.AlterField(
            model_name="prodotto",
            name="Peso",
            field=enumchoicefield.fields.EnumChoiceField(
                enum_class=KindKaribe.models.Peso, max_length=7, null=True
            ),
        ),
    ]
