import csv

from django.contrib import admin
from django.http import HttpResponse
from django.utils.timezone import now

from meetup.subscriptions.models import Subscription

admin.site.site_header = 'Meetup DEVTEC Guaratinguetá'


class SubscriptionModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'subscribed_today')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'created_at')
    list_filter = ('created_at',)

    def subscribed_today(self, obj):
        return obj.created_at == now().date()

    subscribed_today.short_description = 'inscrito hoje?'
    subscribed_today.boolean = True

    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Exportar selecionados"


admin.site.register(Subscription, SubscriptionModelAdmin)


