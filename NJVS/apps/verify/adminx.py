# encoding : utf-8
import xadmin
from verify.models import UserValidate

class ValidateAdmin(object):
    list_display = ('id', 'username', 'validate')

xadmin.site.register(UserValidate, ValidateAdmin)