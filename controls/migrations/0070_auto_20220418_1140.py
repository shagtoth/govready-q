# Generated by Django 3.2.12 on 2022-04-18 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0058_request'),
        ('controls', '0069_alter_element_require_approval'),
    ]

    operations = [
        migrations.AddField(
            model_name='element',
            name='requests',
            field=models.ManyToManyField(related_name='element', to='siteapp.Request'),
        ),
        migrations.AlterField(
            model_name='historicalstatement',
            name='statement_type',
            field=models.CharField(blank=True, choices=[('CONTROL_IMPLEMENTATION', 'control_implementation'), ('CONTROL_IMPLEMENTATION_LEGACY', 'control_implementation_legacy'), ('CONTROL_IMPLEMENTATION_PROTOTYPE', 'control_implementation_prototype'), ('ASSESSMENT_RESULT', 'assessment_result'), ('POAM', 'POAM'), ('SECURITY_SENSITIVITY_LEVEL', 'security_sensitivity_level'), ('SECURITY_IMPACT_LEVEL', 'security_impact_level'), ('COMPONENT_APPROVAL_CRITERIA', 'component_approval_criteria')], help_text='Statement type.', max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='statement',
            name='statement_type',
            field=models.CharField(blank=True, choices=[('CONTROL_IMPLEMENTATION', 'control_implementation'), ('CONTROL_IMPLEMENTATION_LEGACY', 'control_implementation_legacy'), ('CONTROL_IMPLEMENTATION_PROTOTYPE', 'control_implementation_prototype'), ('ASSESSMENT_RESULT', 'assessment_result'), ('POAM', 'POAM'), ('SECURITY_SENSITIVITY_LEVEL', 'security_sensitivity_level'), ('SECURITY_IMPACT_LEVEL', 'security_impact_level'), ('COMPONENT_APPROVAL_CRITERIA', 'component_approval_criteria')], help_text='Statement type.', max_length=150, null=True),
        ),
    ]