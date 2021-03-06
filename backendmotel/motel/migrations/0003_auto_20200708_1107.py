# Generated by Django 3.0.7 on 2020-07-08 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('motel', '0002_auto_20200707_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemotel',
            name='motel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='motel', to='motel.Motel'),
        ),
        migrations.AlterField(
            model_name='motel',
            name='district',
            field=models.CharField(choices=[('1', 'Quận 1'), ('2', 'Quận 2'), ('3', 'Quận 3'), ('4', 'Quận 4'), ('5', 'Quận 5'), ('6', 'Quận 6'), ('7', 'Quận 7'), ('8', 'Quận 8'), ('9', 'Quận 9'), ('10', 'Quận 10'), ('11', 'Quận 11'), ('12', 'Quận 12'), ('13', 'Quận Bình Tân'), ('14', 'Quận Bình Thạnh'), ('15', 'Quận Gò Vấp'), ('16', 'Quận Phú Nhuận'), ('17', 'Quận Tân Bình'), ('18', 'Quận Tân Phú'), ('18', 'Quận Thủ Đức'), ('20', 'Huyện Bình Chánh'), ('21', 'Huyện Cần Giờ'), ('22', 'Huyện Củ Chi'), ('23', 'Huyện Hóc Môn'), ('24', 'Huyện Nhà Bè')], db_index=True, default='1', max_length=3),
        ),
    ]
