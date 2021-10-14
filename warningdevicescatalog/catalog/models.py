"""Create your models here."""
from django.db import models


class WarningDevice(models.Model):
    """Model for create table WarningDevice."""

    name = models.CharField(max_length=40, verbose_name="Название")
    type_device = models.CharField(verbose_name="Тип устройста", choices=(
        ("Сирена", "Сирена"),
        ("Громкоговоритель", "Громкоговоритель")),
        max_length=16)
    adress_location = models.CharField(
        max_length=200, verbose_name="Адрес размещения")
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Долгота")
    zone_radius = models.IntegerField(verbose_name="Радиус зоны звукопокрытия")

    def save(self, *args, **kwargs):
        """Functin for round value latitude and longitude."""
        self.latitude = round(self.latitude, 6)
        self.longitude = round(self.longitude, 6)
        super(WarningDevice, self).save(*args, **kwargs)

    class Meta:
        """Change name list objects."""

        verbose_name = "Устройство оповещения"
        verbose_name_plural = "Устройства оповещения"

    def __str__(self):
        """Chane name for string display."""
        return (str(self.name))
