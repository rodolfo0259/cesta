# Generated by Django 4.0.5 on 2022-06-15 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_familiaatendida_ativo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiaatendida',
            name='bairro',
            field=models.CharField(blank=True, help_text='Informe o bairro do endereço', max_length=30, null=True, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='familiaatendida',
            name='complemento',
            field=models.CharField(blank=True, help_text='Informe o complemento do endereço', max_length=30, null=True, verbose_name='Complemento'),
        ),
        migrations.AlterField(
            model_name='familiaatendida',
            name='logradouro',
            field=models.CharField(blank=True, help_text='Informe o logradouro e número do endereço', max_length=50, null=True, verbose_name='Logradouro'),
        ),
        migrations.AlterField(
            model_name='familiaatendida',
            name='observacoes',
            field=models.CharField(blank=True, help_text='Informe observações importantes', max_length=255, null=True, verbose_name='Observações'),
        ),
        migrations.AlterField(
            model_name='familiaatendida',
            name='telefone',
            field=models.CharField(blank=True, help_text='Informe os telefones de contato', max_length=50, null=True, verbose_name='Telefone'),
        ),
    ]
