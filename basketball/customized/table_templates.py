# -*-coding:utf-8 -*-
CREDIT_TEMPLATES={"TABLE_5_TEAMS":"""
<table id="#group_id#">
    <thead>
        <tr>
            <th></th>
            <th>#1#</th>
            <th>#2#</th>
            <th>#3#</th>
            <th>#4#</th>
            <th>#5#</th>
            <th>积分</th>
            <th>排名</th>
        </tr>
    </thead>
    <tbody>
        <tr><th>#1#</th><th></th><td></td><td></td><td></td><td></td><td></td><td></td></tr>
        <tr><th>#2#</th><td></td><th></th><td></td><td></td><td></td><td></td><td></td></tr>
        <tr><th>#3#</th><td></td><td></td><th></th><td></td><td></td><td></td><td></td></tr>
        <tr><th>#4#</th><td></td><td></td><td></td><th></th><td></td><td></td><td></td></tr>
        <tr><th>#5#</th><td></td><td></td><td></td><td></td><th></th><td></td><td></td></tr>
    </tbody>
    </table>
"""
,
"TABLE_6_TEAMS":"""
<table id="#group_id#">
    <thead>
        <tr>
            <th></th>
            <th>#1#</th>
            <th>#2#</th>
            <th>#3#</th>
            <th>#4#</th>
            <th>#5#</th>
            <th>#6#</th>
            <th>积分</th>
            <th>排名</th>
        </tr>
    </thead>
    <tbody>
        <tr><th>#1#</th><th></th><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
        <tr><th>#2#</th><td></td><th></th><td></td><td></td><td></td><td></td><td></td><td></td></tr>
        <tr><th>#3#</th><td></td><td></td><th></th><td></td><td></td><td></td><td></td><td></td></tr>
        <tr><th>#4#</th><td></td><td></td><td></td><th></th><td></td><td></td><td></td><td></td></tr>
        <tr><th>#5#</th><td></td><td></td><td></td><td></td><th></th><td></td><td></td><td></td></tr>
        <tr><th>#6#</th><td></td><td></td><td></td><td></td><td></td><th></th><td></td><td></td></tr>
    </tbody>
    </table>
"""
,
"TABLE_7_TEAMS":"""
<table id="#group_id#">
    <thead>
        <tr>
            <th></th>
            <th>#1#</th>
            <th>#2#</th>
            <th>#3#</th>
            <th>#4#</th>
            <th>#5#</th>
            <th>#6#</th>
            <th>#7#</th>
            <th>积分</th>
            <th>排名</th>
        </tr>
    </thead>
    <tbody>
        <tr><th>#1#</th><th></th><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
        <tr><th>#2#</th><td></td><th></th><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr>
        <tr><th>#3#</th><td></td><td></td><th></th><td></td><td></td><td></td><td></td><td></td><td></td></tr>
        <tr><th>#4#</th><td></td><td></td><td></td><th></th><td></td><td></td><td></td><td></td><td></td></tr>
        <tr><th>#5#</th><td></td><td></td><td></td><td></td><th></th><td></td><td></td><td></td><td></td></tr>
        <tr><th>#6#</th><td></td><td></td><td></td><td></td><td></td><th></th><td></td><td></td><td></td></tr>
        <tr><th>#7#</th><td></td><td></td><td></td><td></td><td></td><td></td><th></th><td></td><td></td></tr>
    </tbody>
    </table>
"""
}

GAME_TEMPLATES={
	"TABLE_GAME":"""
	<section class="level">
		<h3>2019-8-7</h3>
		<table>
			<thead>
				<tr>
					<th>日期</th>
					<th>时间</th>
					<th>甲队得分</th>
					<th>甲队</th>
					<th>乙队</th>
					<th>乙队得分</th>
					<th>级别</th>
					<th>组别</th>
				</tr>
			</thead>
		</table>
	</section>
	"""
}

# For generating credit table
def generate_credit_table(year,league):
    search_dict0 = dict()
    search_dict0['league_year'] = year
    search_dict0['league'] = league
    levels = Team.objects.values('team_level').filter(**search_dict0).distinct()
    levels_dict = {}
    for l in list(levels):
        search_dict = dict()
        search_dict['team_level'] = l['team_level']
        search_dict['league_year'] = year
        search_dict['league'] = league
        groups = Team.objects.values('team_group').filter(**search_dict).distinct()
        groups_arr = []
        for g in groups:
            groups_dict = {}
            search_dict2 = dict()
            search_dict2['team_group'] = g['team_group']
            search_dict2['league_year'] = year
            search_dict2['league'] = league
            teams = Team.objects.values('team_group_no','team_nick_name').filter(**search_dict2)
            group_id = "group_%s"%(g['team_group'].lower())
            temp = "TABLE_%d_TEAMS"%len(teams)
            template = table_templates.CREDIT_TEMPLATES[temp].replace('#group_id#',group_id)
            for i in range(len(teams)):
                num = "#%d#" % (i+1)
                t_n = teams[i]['team_group_no']+":"+teams[i]['team_nick_name']
                template = template.replace(num,t_n)
            groups_dict[g['team_group']] = template
            groups_arr.append(groups_dict)
        levels_dict[l['team_level']] = groups_arr
    
    return levels_dict