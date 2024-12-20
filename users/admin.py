from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Discipline, Match, PlayerSlot

# CustomUser Admin
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {
            'fields': (
                'first_name', 'last_name', 'email', 'nickname', 
                'date_of_birth', 'gender', 'height', 'height_unit', 
                'weight', 'weight_unit', 'country', 'disability'
            )
        }),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('email',)

# Discipline Admin
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'favorite_position', 'dominant_foot')
    search_fields = ('user__username', 'name')
    list_filter = ('name', 'created_at')
    ordering = ('user', 'name')

# Match Admin
class MatchAdmin(admin.ModelAdmin):
    list_display = ('place', 'date_time', 'player_count', 'formation', 'creator')
    search_fields = ('place', 'creator__username')
    list_filter = ('date_time', 'formation', 'field_type')
    ordering = ('-date_time',)

# PlayerSlot Admin
class PlayerSlotAdmin(admin.ModelAdmin):
    list_display = ('match', 'slot_number', 'player', 'is_captain')
    search_fields = ('match__place', 'player__username')
    list_filter = ('is_captain',)
    ordering = ('match', 'slot_number')

# Register Models
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Discipline, DisciplineAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(PlayerSlot, PlayerSlotAdmin)
