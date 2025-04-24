from django.contrib import admin

from .models import StockQuotes, Company


admin.site.register(Company)

class StockQuotesAdmin(admin.ModelAdmin):
    list_display = ('company__ticker','close_price', 'time')
    list_filter = ('company__ticker', 'time')

admin.site.register(StockQuotes, StockQuotesAdmin)