# -*-coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Team, Game
import json
import datetime
import collections
from django.contrib.admin.views.decorators import staff_member_required

def index(request):
    leagues = Team.objects.values('league','league_year').distinct()
    return render(request, 'basketball/index.html',{'data':list(leagues)})

def home(request):
    league_info = check_params(request)
    if league_info:
        league_info.append('home')
        return render(request, 'basketball/basketball.html',{'data': {'data':'','league_info':league_info}})
    else:
        error_info = "Error! Method:GET Usage: /home?league=zjb&year=2019"
        return HttpResponse(error_info)

def teams(request):
    league_info = check_params(request)
    if league_info:
        league_info.append('teams')
        search_dict={'league':league_info[0],'league_year':league_info[1]}
        teams = Team.objects.values('team_level','team_id','team_group_no',
            'team_name','team_nick_name').filter(**search_dict).order_by('team_group_no')
        return render(request, 'basketball/basketball.html',{'data': {'data':list(teams),'league_info':league_info}})
    else:
        error_info = "Error! Method:GET Usage: /teams?league=zjb&year=2019"
        return HttpResponse(error_info)

def schedule(request):
    league_info = check_params(request)
    if league_info:
        league_info.append('schedule')
        games = get_schedule_data(league_info[0],league_info[1],'r')
        return render(request, 'basketball/basketball.html',{'data': {'data':list(games),'league_info':league_info}})
    else:
        error_info = "Error! Method:GET Usage: /schedule?league=zjb&year=2019"
        return HttpResponse(error_info)

def credit(request):
    league_info = check_params(request)
    if league_info:
        league_info.append('credit')
        teams = get_credit_data(league_info[0],league_info[1])
        complete_games = get_complete_games(league_info[0],league_info[1])
        return render(request, 'basketball/basketball.html',{'data': 
            {'data':json.dumps(teams),'league_info':league_info,'complete_games':complete_games}})
    else:
        error_info = "Error! Method:GET Usage: /credit?league=zjb&year=2019"
        return HttpResponse(error_info)

def playoff(request):
    league_info = check_params(request)
    if league_info:
        league_info.append('playoff')
        games = get_schedule_data(league_info[0],league_info[1],'p')
        return render(request, 'basketball/basketball.html',{'data': {'data':list(games),'league_info':league_info}})
    else:
        error_info = "Error! Method:GET Usage: /credit?league=zjb&year=2019"
        return HttpResponse(error_info)

def update_credit(request):
    if request.method == "POST":
        data = request.POST['data']
        data = json.loads(data)
    league_info = data['league_info']
    search_dict = {'league':league_info[0],'league_year':league_info[1]}
    for k,v in data.items():
        if k != 'league_info':
            group = k[-1]
            for key,val in v.items():
                search_dict['team_group_no'] = group+key
                update_team_model(search_dict,val)
    return HttpResponse('Updated Credit successfully.')

def update_team_model(search_dict,value):
    _ts = Team.objects.filter(**search_dict)
    for _t in _ts:
        _t.team_credit = value
        _t.save()

def check_params(request):
    if request.method =="GET":
        if 'league' in request.GET and 'year' in request.GET:
            league = request.GET['league']
            year = request.GET['year']
            return [league,year]
        else:
            return False
    else:
        return False

# For getting the credit data
def get_credit_data(league,year):
    search_dict = {'league':league,'league_year':year}
    levels = Team.objects.values('team_level').filter(**search_dict).distinct()
    print(levels)
    levels_dict = collections.OrderedDict()
    for l in list(levels):
        search_dict['team_level'] = l['team_level']
        groups = Team.objects.values('team_group').filter(**search_dict).distinct()
        groups_arr = []
        for g in groups:
            groups_dict = {}
            search_dict1 = {'league':league,'league_year':year,'team_group':g['team_group']}
            teams = Team.objects.values('team_group_no','team_nick_name','team_rank').filter(**search_dict1)
            groups_dict[g['team_group']] = list(teams)
            groups_arr.append(groups_dict)
        levels_dict[l['team_level']] = groups_arr
    return levels_dict

def get_complete_games(league,year):
    search_dict = {'league':league,'league_year':year,'game_complete':True}
    games = Game.objects.values('team_a_group_no','team_a_score','team_b_group_no','team_b_score').filter(**search_dict)
    return list(games)

# For getting the schedule data
def get_schedule_data(league,year,game_type):
    search_dict = dict()
    search_dict['league_year'] = year
    search_dict['league'] = league
    search_dict['game_type'] = game_type
    games = Game.objects.values('game_id','team_a','team_a_score','team_b','team_b_score','game_date','game_start_time',
        'game_level','game_group','game_complete','game_court').filter(**search_dict)
    for i in games:
        for k,v in i.items():
            i[k]=convert_datetime(v)
        print(i)
    return games

def convert_datetime(o):
    DATE_FORMAT = "%Y-%m-%d" 
    TIME_FORMAT = "%H:%M"
    if isinstance(o, datetime.date):
        return o.strftime(DATE_FORMAT)
    elif isinstance(o, datetime.time):
        return o.strftime(TIME_FORMAT)
    elif isinstance(o, datetime.datetime):
        return o.strftime("%s %s" % (DATE_FORMAT, TIME_FORMAT))
    elif isinstance(o, bool):
        return str(o)
    elif o == None:
        return ""
    else:
        return o



def update_playoff(request):
    return render(request, "basketball/update_playoff.html")

update_playoff = staff_member_required(update_playoff)
