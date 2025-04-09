from django.contrib import admin
from action.models import User,Image,Blackboard ,Text
# Register your models here.


admin.site.register(User)
admin.site.register(Text)
admin.site.register(Image)
admin.site.register(Blackboard)