from django.contrib import admin #type: ignore

from .models import FootballPlayer



@admin.register(FootballPlayer)
class FootballPlayerAdmin(admin.ModelAdmin):
    list_display = ('index', 'Player', 'number', 'Nation', 'Pos', 'Age', 'Min', 'Gls', 'Ast', 'PK', 'PKatt', 'Sh', 'SoT', 'CrdY', 'CrdR', 'Touches', 'Tkl', 'Int', 'Blocks', 'xG', 'npxG', 'xAG', 'SCA', 'GCA', 'Cmp_x', 'Att_x', 'Cmp_pct_x', 'PrgP', 'Carries', 'PrgC', 'Att_x_alt', 'Succ', 'SoTA', 'GA', 'Saves', 'Save_pct', 'PSxG', 'Cmp_y', 'Att_y', 'Cmp_pct_y', 'Att_GK', 'Thr', 'Launch_pct', 'AvgLen', 'Opp')
    search_fields = ['Player', 'Nation', 'Pos']
    list_filter = ['Nation', 'Pos']
    ordering = ['Player']
    list_per_page = 20