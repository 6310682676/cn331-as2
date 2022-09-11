from django.contrib import admin

#from users.models import Account
from users.models import Booking

# Register your models here.
admin.site.register(Booking)

'''class AccountInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'Accounts'

admin.site.unregister(User)
admin.site.register(User, )'''