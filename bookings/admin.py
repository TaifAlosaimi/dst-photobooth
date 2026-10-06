from django.contrib import admin

from .models import Booking, Package


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "duration_hours", "photo_count")


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "event_type", "event_date", "package", "status")