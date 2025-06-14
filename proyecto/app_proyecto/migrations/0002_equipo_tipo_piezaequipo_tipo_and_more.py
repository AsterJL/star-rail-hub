# Generated by Django 5.1.3 on 2025-06-09 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_proyecto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='tipo',
            field=models.CharField(choices=[('Principal', 'Principal'), ('Secundario', 'Secundario')], default='Principal', max_length=100, verbose_name='Tipo'),
        ),
        migrations.AddField(
            model_name='piezaequipo',
            name='tipo',
            field=models.CharField(choices=[('Casco', 'Casco'), ('Manos', 'Manos'), ('Pecho', 'Pecho'), ('Botas', 'Botas'), ('Orbe', 'Orbe'), ('Cuerda', 'Cuerda')], default='Casco', max_length=100, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='afiliacion',
            name='descripcion',
            field=models.CharField(max_length=2000, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='arma',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='elementopersonaje',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='enemigo',
            name='descripcion',
            field=models.CharField(max_length=2000, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='enemigo',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='bono',
            field=models.CharField(max_length=2000, verbose_name='Bono'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='funcion',
            name='descripcion',
            field=models.CharField(max_length=2000, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='funcion',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='habilidadarma',
            name='descripcion',
            field=models.CharField(max_length=2000, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='habilidadarma',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='habilidadpersonaje',
            name='descripcion',
            field=models.CharField(max_length=2000, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='habilidadpersonaje',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='habilidadpersonaje',
            name='tipo',
            field=models.CharField(choices=[('Activa', 'Activa'), ('Pasiva', 'Pasiva')], default='Activa', max_length=100, verbose_name='Tipo'),
        ),
        migrations.AlterField(
            model_name='imagenarma',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='imagenmapa',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='imagenpersonaje',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='material',
            name='descripcion',
            field=models.CharField(max_length=2000, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='material',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='metodoobtencion',
            name='metodo',
            field=models.CharField(max_length=300, verbose_name='Método'),
        ),
        migrations.AlterField(
            model_name='personaje',
            name='descripcion',
            field=models.CharField(blank=True, max_length=2000, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='personaje',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='personaje',
            name='titulo',
            field=models.CharField(blank=True, max_length=100, verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='piezaequipo',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='rareza',
            name='nombre',
            field=models.CharField(max_length=100, verbose_name='Nombre'),
        ),
    ]
