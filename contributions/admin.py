from django.contrib import admin
from contributions.models import media
from contributions.models import book
from contributions.models import customer
from contributions.models import order

admin.site.register(media)
admin.site.register(book)
admin.site.register(customer)
admin.site.register(order)