from django.contrib import admin
from dispatcher.models import Users, Landmarks, Cities, LMSuggestion

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Users, AuthorAdmin)
admin.site.register(Landmarks, AuthorAdmin)
admin.site.register(Cities, AuthorAdmin)
admin.site.register(LMSuggestion, AuthorAdmin)