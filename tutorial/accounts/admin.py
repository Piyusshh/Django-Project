from django.contrib import admin
from accounts.models import UserProfile  # ye import isliye kiye kyunki humne model account folder me "models" me banaya tha

# Register your models here.

############      admin.site.register(UserProfile)

#admin.site.site_header = 'Customized Django Admin'

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','user_info','city','phone','website')

    def user_info(self, obj):
        return obj.description

    def get_queryset(self, request):  # for sorting all the query according to requirement
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-phone','user')
        return queryset

    user_info.short_description = 'Info'  # from user info -> info
    
admin.site.register(UserProfile, UserProfileAdmin)