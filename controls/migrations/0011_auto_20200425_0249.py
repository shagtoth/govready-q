# Generated by Django 2.2.12 on 2020-04-25 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controls', '0010_auto_20200424_0849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statement',
            name='described_element',
        ),
        migrations.RemoveField(
            model_name='statement',
            name='referenced_elements',
        ),
        migrations.AddField(
            model_name='statement',
            name='consumer_element',
            field=models.ForeignKey(blank=True, help_text='The element the statement is about. ', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='statements_consumed', to='controls.Element'),
        ),
        migrations.AddField(
            model_name='statement',
            name='mentioned_elements',
            field=models.ManyToManyField(blank=True, help_text='All elements mentioned in a statement; elements with a first degree relationship to the statement.', related_name='statements_mentioning', to='controls.Element'),
        ),
        migrations.AddField(
            model_name='statement',
            name='producer_element',
            field=models.ForeignKey(blank=True, help_text='The element producing this statement. ', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='statements_produced', to='controls.Element'),
        ),
    ]
