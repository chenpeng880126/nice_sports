from django.contrib import admin
from .models import Team,Game

admin.site.site_header = 'Nice Basketball'
admin.site.site_title = 'Nice Basketball Admin'

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display=('team_id','league','league_year','team_name','team_nick_name',
                 'team_level','team_group','team_group_no','team_credit','team_rank')
    list_per_page = 30
    ordering = ('team_id',)
    list_filter = ('league','league_year','team_level','team_group')
    search_fields = ('team_id', 'team_name', 'team_level','team_group','team_group_no')
    list_editable = ('team_nick_name','team_rank')

    def get_queryset(self,request):
        qs = super(TeamAdmin,self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        elif str(request.user) in ['ldl']:
            return qs.filter(league='zjb')
        elif str(request.user) in ['lwb']:
            return qs.filter(league='hhb')
        return qs

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display=('game_id','team_a_score','team_a_group_no','team_a','team_b','team_b_group_no','team_b_score','game_complete',
        'game_type','game_date','game_start_time','game_group','league','league_year')
    list_per_page = 50
    ordering = ('game_id',)
    list_filter = ('league','game_date','game_type','game_level','league_year','game_group')
    search_fields = ('game_id', 'team_a', 'team_b','game_group','game_date')
    list_editable = ('team_a_score', 'team_b_score','game_complete')
    date_hierarchy = 'game_date'

    def get_queryset(self,request):
        qs = super(GameAdmin,self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        elif str(request.user) in ['ldl']:
            return qs.filter(league='zjb')
        elif str(request.user) in ['lwb']:
            return qs.filter(league='hhb')
        return qs