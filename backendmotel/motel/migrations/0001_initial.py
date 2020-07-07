# Generated by Django 3.0.7 on 2020-07-06 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageMotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='motel/')),
            ],
        ),
        migrations.CreateModel(
            name='Motel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('content', models.TextField(blank=True, null=True)),
                ('typeMotel', models.CharField(choices=[('A', 'Phòng Trọ'), ('B', 'Nhà Nguyên Căn'), ('C', 'Chung Cư'), ('D', 'Nhà Phố'), ('E', 'Nhà Ở Ghép')], db_index=True, default='A', max_length=1)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('ward', models.CharField(blank=True, max_length=100)),
                ('district', models.CharField(choices=[('Q01', 'Quận 1'), ('Q02', 'Quận 2'), ('Q03', 'Quận 3'), ('Q04', 'Quận 4'), ('Q05', 'Quận 5'), ('Q06', 'Quận 6'), ('Q07', 'Quận 7'), ('Q08', 'Quận 8'), ('Q09', 'Quận 9'), ('Q10', 'Quận 10'), ('Q11', 'Quận 11'), ('Q12', 'Quận 12'), ('BTA', 'Quận Bình Tân'), ('BTH', 'Quận Bình Thạnh'), ('QGV', 'Quận Gò Vấp'), ('QPN', 'Quận Phú Nhuận'), ('QTB', 'Quận Tân Bình'), ('QTP', 'Quận Tân Phú'), ('QTD', 'Quận Thủ Đức'), ('HBC', 'Huyện Bình Chánh'), ('HCG', 'Huyện Cần Giờ'), ('HCC', 'Huyện Củ Chi'), ('HHM', 'Huyện Hóc Môn'), ('HNB', 'Huyện Nhà Bè')], db_index=True, default='Q01', max_length=3)),
                ('phone_number', models.CharField(blank=True, max_length=10)),
                ('arc', models.PositiveIntegerField(blank=True, default=1)),
                ('price', models.PositiveIntegerField(default=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
            ],
        ),
    ]
