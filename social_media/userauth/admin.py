from django.contrib import admin

# Register your models here.
from .models import *

# Profile ve Post modellerini yönetilebilir hale getir!

admin.site.register(Profile)  
admin.site.register( Post)
admin.site.register( LikePost)
admin.site.register( Followers)

