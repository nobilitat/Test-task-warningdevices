"""Register your models here."""
from catalog.models import WarningDevice

from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class CountryFilter(admin.SimpleListFilter):
    """Class with custom user filter."""

    title = 'Радиус зоны звукопокрытия'
    parameter_name = 'zone_radius'

    def lookups(self, request, model_admin):
        """Варианты выбора фильтрации."""
        return (
            ('100м', _('радиус 100м')),
            ('200м', _('радиус 200м')),
            ('300м', _('радиус 300м')),
            ('400м', _('радиус 400м')),
            ('500м', _('радиус 500м')),
        )

    def queryset(self, request, queryset):
        """Возвращение соответствующего значения выбору."""
        if self.value() == '100м':
            return queryset.filter(zone_radius=100)
        if self.value() == '200м':
            return queryset.filter(zone_radius=200)
        if self.value() == '300м':
            return queryset.filter(zone_radius=300)
        if self.value() == '400м':
            return queryset.filter(zone_radius=400)
        if self.value() == '500м':
            return queryset.filter(zone_radius=500)


class AdminWarningDevices(admin.ModelAdmin):
    """Adminclass for display in django-admin."""

    model = WarningDevice
    list_display = ("id", "name", "type_device", "zone_radius", )
    list_display_links = ("id", "name", )
    search_fields = ("name", "adress_location")
    list_filter = ("type_device", CountryFilter)


admin.site.register(WarningDevice, admin_class=AdminWarningDevices)
