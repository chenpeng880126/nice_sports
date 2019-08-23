var SCHEDULE_TABLE="<section class='level'><h3>#date#</h3><table id=#date#>"+
	"<thead><tr><th>时间</th><th>甲队得分</th><th>甲队</th><th>乙队</th"+
	"><th>乙队得分</th><th>级别</th><th>组别</th><th>场地</th></tr></thead>"+
	"<tbody id='#tbody_id#'></tbody></table></section>";

var PLAYOFF_TABLE="<section class='level'><h3>#date#</h3><table id=#date#>"+
	"<thead><tr><th>比赛序号</th><th>时间</th><th>甲队得分</th><th>甲队</th><th>乙队</th"+
	"><th>乙队得分</th><th>级别</th><th>场地</th></tr></thead>"+
	"<tbody id='#tbody_id#'></tbody></table></section>";

var TEAM_TABLE="<section class='level' id='#level#'><h3>#level#</h3><table>"+
	"<thead><tr><th>球队ID</th><th>球队组别</th><th>球队名称</th><th>球队简称</th></tr></thead>"+
	"<tbody id='#tbody_id#'></tbody></table></section>";

var CREDIT_TABLE_HEADER="<section class='level' id='#level#'><h3>#level#</h3></section>"
var CREDIT_TABLE={
	3:"<table id='#group_id#'><thead><tr><th>#num#组</th><th>#team_0#</th><th>#team_1#</th><th>#team_2#</th><th>积分</th><th>排名</th></tr></thead><tbody></tbody></table>",
	4:"<table id='#group_id#'><thead><tr><th>#num#组</th><th>#team_0#</th><th>#team_1#</th><th>#team_2#</th><th>#team_3#</th><th>积分</th><th>排名</th></tr></thead><tbody></tbody></table>",
	5:"<table id='#group_id#'><thead><tr><th>#num#组</th><th>#team_0#</th><th>#team_1#</th><th>#team_2#</th><th>#team_3#</th><th>#team_4#</th><th>积分</th><th>排名</th></tr></thead><tbody></tbody></table>",
	6:"<table id='#group_id#'><thead><tr><th>#num#组</th><th>#team_0#</th><th>#team_1#</th><th>#team_2#</th><th>#team_3#</th><th>#team_4#</th><th>#team_5#</th><th>积分</th><th>排名</th></tr></thead><tbody></tbody></table>",
	7:"<table id='#group_id#'><thead><tr><th>#num#组</th><th>#team_0#</th><th>#team_1#</th><th>#team_2#</th><th>#team_3#</th><th>#team_4#</th><th>#team_5#</th><th>#team_6#</th><th>积分</th><th>排名</th></tr></thead><tbody></tbody></table>",
	8:"<table id='#group_id#'><thead><tr><th>#num#组</th><th>#team_0#</th><th>#team_1#</th><th>#team_2#</th><th>#team_3#</th><th>#team_4#</th><th>#team_5#</th><th>#team_6#</th><th>#team_7#<</th><th>积分</th><th>排名</th></tr></thead><tbody></tbody></table>",
}


var PAGE_HEADER={
	"home":"<h2 style='text-align: center;'>嘿，兄弟，一起肩并肩作战吧！</h2>",
	"teams":"<header><h2>球队概览</h2><p id='league_desc'></p></header>",
	"schedule":"<header><h2>赛程安排</h2></header>",
	"credit":"<header><h2>积分规则</h2></header><p>"+
			"概述：球队应按他们的胜负记录来排列名次，胜1场得2分，负1场(包括比赛因缺少队员告负)得1分，比赛因弃权告负得0分。<br/>"+
			"1、如果在这个排列中两个球队积分相等，则以两个队之间比赛的结果来确定名次。 <br/>"+
			"2、如果两个队之间在比赛中的积分和得失分率仍相同，则以两个队在组内所有比赛的得失分率来确定名次。 <br/>"+
			"3、如果在排列中有两个以上的球队积分相等，需要建立第二个排列，此排列将只把积分相等的球队之间的比赛结果考虑进去。 <br/>"+
			"4、如果在任何阶段，用上述准则将众多排列相同的球队减缩到只包含两个球队排列相同，则应使用上述1款和2款程序。<br />"+
			"5、如果再次排列后仍有球队积分相同，则只考虑相同的球队之间的比赛结果，用其得失分率来确定名次。 <br />"+
			"6、如果仍有两个以上球队得失分率相同，用其组内所有比赛结果的得失分率来确定名次。 <br />"+
			"7、如果在任何阶段，减缩后积分相等的球队仍是两个以上，则从上述3程序开始重复。 <br />"+
			"8、得失分率总是用除法来计算。 第2款例外: 如果只有三个球队参加比赛，并用上述的步骤(除得的得失分率完全相同)不能决出名次，则用得分来确定名次排列。 </p>",
	"playoff":"<header><h2>爆燃季后赛</h2></header>"
}

var LEAGUE_MAP={'zjb':'张江杯','hhb':'浩瀚杯'}

function table_init(){
	$('table').stickySort({ sortable: false });
	$('table th,tr,td').css({"font-size":"12px"});
	
	
	$('section.level h3')
		.append('<a href="#" title="Collapse section" class="toggle">Collapse</a>')
		.on('click', 'a', function(e) {
			e.preventDefault();
			
			if(!$(this).data('state') || $(this).data('state') == 0) {
				$(this)
				.data('state', 1)
				.attr('title', 'Expand section')
				.text('Expand')
				.parent()
					.siblings()
						.stop(true,true).slideUp();
			} else {
				$(this)
				.data('state', 0)
				.attr('title', 'Collapse section')
				.text('Collapse')
				.parent()
					.siblings()
						.stop(true,true).slideDown();
			}
		});

	$('a.toggle').css({"background-color":'#B22222'})
};

function generate_teams_table(data){
	$('#league_desc').text('共有'+data.length+'支队伍')
	for(var i=0;i<data.length;i++){
		level = data[i].team_level;
		if(level == ''){
			level = '同一级别'
		}
		if ($('#'+level).size() == 0){
			team_table = TEAM_TABLE.replace(/#level#/g,level)
			team_table = team_table.replace('#tbody_id#','tbody_'+level)
			$('#main-content').append(team_table);
		}
		$('#tbody_'+level).append("<tr><td>"+data[i].team_id+
			"</td><td>"+data[i].team_group_no+
			"</td><td>"+data[i].team_name+
			"</td><td>"+data[i].team_nick_name+
			"</td>");
		
	}
}

function generate_schedule_table(data){
	for(var k in data){
		game_date = data[k]['game_date']
		is_complete = data[k]['game_complete']
		game_id = data[k]['game_id']
		team_a_score = parseInt(data[k]['team_a_score'])
		team_b_score = parseInt(data[k]['team_b_score'])

		if($('#'+game_date).size() == 0){
			schedule_table = SCHEDULE_TABLE.replace(/#date#/g,game_date);
			schedule_table = schedule_table.replace('#tbody_id#','tbody_'+game_date);
			$('#main-content').append(schedule_table);
		}
		$('#tbody_'+game_date).append(
			"<tr id='"+game_id+"'><td>"+data[k]['game_start_time']+
			"</td><td>"+data[k]['team_a_score']+
			"</td><td>"+data[k]['team_a']+
			"</td><td>"+data[k]['team_b']+
			"</td><td>"+data[k]['team_b_score']+
			"</td><td>"+data[k]['game_level']+
			"</td><td>"+data[k]['game_group']+
			"</td><td>"+data[k]['game_court']+
			"</td></tr>");
		
		if(is_complete=="True"){
			$('#'+game_id).css({'background-color':'#00FFFF'});
		}

		if(team_a_score > team_b_score){
			$('#'+game_id+' td:eq(1)').css({'color':'#FF4500','font-weight':'bold'});
			$('#'+game_id+' td:eq(2)').css({'color':'#FF4500','font-weight':'bold'});
		}else if(team_a_score < team_b_score){
			$('#'+game_id+' td:eq(3)').css({'color':'#FF4500','font-weight':'bold'});
			$('#'+game_id+' td:eq(4)').css({'color':'#FF4500','font-weight':'bold'});
		}
	}
}	

function generate_playoff_table(data){
	for(var k in data){
		game_date = data[k]['game_date']
		is_complete = data[k]['game_complete']
		game_id = data[k]['game_id']
		team_a_score = parseInt(data[k]['team_a_score'])
		team_b_score = parseInt(data[k]['team_b_score'])

		if($('#'+game_date).size() == 0){
			playoff_table = PLAYOFF_TABLE.replace(/#date#/g,game_date);
			playoff_table = playoff_table.replace('#tbody_id#','tbody_'+game_date);
			$('#main-content').append(playoff_table);
		}
		$('#tbody_'+game_date).append(
			"<tr id='"+game_id+"'><td>"+game_id.slice(9)+
			"</td><td>"+data[k]['game_start_time']+
			"</td><td>"+data[k]['team_a_score']+
			"</td><td>"+data[k]['team_a']+
			"</td><td>"+data[k]['team_b']+
			"</td><td>"+data[k]['team_b_score']+
			"</td><td>"+data[k]['game_level']+
			//"</td><td>"+data[k]['game_group']+
			"</td><td>"+data[k]['game_court']+
			"</td></tr>");
		
		if(is_complete=="True"){
			$('#'+game_id).css({'background-color':'#00FFFF'});
		}

		if(team_a_score > team_b_score){
			$('#'+game_id+' td:eq(1)').css({'color':'#FF4500','font-weight':'bold'});
			$('#'+game_id+' td:eq(2)').css({'color':'#FF4500','font-weight':'bold'});
		}else if(team_a_score < team_b_score){
			$('#'+game_id+' td:eq(3)').css({'color':'#FF4500','font-weight':'bold'});
			$('#'+game_id+' td:eq(4)').css({'color':'#FF4500','font-weight':'bold'});
		}
	}
}	

function generate_credit_table(data){
	for(var level in data){
		var origin_level = level.replace(' ','');
		/*
		if(origin_level == '') origin_level='null';
		
		if(origin_level == 'null' ){
			origin_level = '同一级别'
		}
		console.log(origin_level)*/
		if ($('#'+origin_level).size() == 0){
			var credit_table_h = CREDIT_TABLE_HEADER.replace(/#level#/g,origin_level)
			$('#main-content').append(credit_table_h);
		}
		for(var i in data[level]){
			for(var k in data[level][i]){
				var teams = data[level][i][k];
				//console.log(teams)
				var t_q = teams.length;
				var credit_table = CREDIT_TABLE[t_q].replace('#group_id#','group_'+k);
				credit_table = credit_table.replace('#num#',k);
				var nick_name = ''
				for(var j in teams){
					nick_name = teams[j]['team_nick_name'];
					credit_table = credit_table.replace('#team_'+j+'#',nick_name)
				}
				$('#'+origin_level).append(credit_table);
				var tds = ''
				for(var n =0;n<t_q+2;n++){
					tds += '<td></td>'
				}
				for(var j in teams){
					nick_name = teams[j]['team_nick_name'];
					$('#group_'+k+' tbody').append('<tr><th>'+nick_name+'</th>'+tds+'</tr>');
					$('#group_'+k+' tbody tr:eq('+ j +')').children('td').eq(-1).text(teams[j]['team_rank']);
					$('#group_'+k+' tbody tr:eq('+ j +') td:eq('+ j +')').css("background-color","#A9A9A9");
				}
			}
		}
	}
	$('table th,tr,td').css(
		{"border":"1px solid #ccc",
		"border-collapse":"collapse",
		"width":"60px",
		"text-align":"center",
	});
}

//需要确保球队分组信息正确
function fill_up_credit(complete_games){

	var regExp = /([a-zA-Z])(\d)/;
	for(i in complete_games){
		g = complete_games[i]
		res = regExp.exec(g['team_a_group_no'])
		group_no = res[1]
		team_a = res[2]
		team_a_score = g['team_a_score']
		team_b = regExp.exec(g['team_b_group_no'])[2]
		team_b_score = g['team_b_score']
		loc_a = '#group_'+group_no+' tbody tr:eq('+ (parseInt(team_a)-1) +') td:eq('+(parseInt(team_b)-1)+')';
		loc_b = '#group_'+group_no+' tbody tr:eq('+ (parseInt(team_b)-1) +') td:eq('+(parseInt(team_a)-1)+')';
		if (parseInt(team_a_score)>parseInt(team_b_score)){
			a_score = team_a_score+":"+team_b_score+"|2";
			b_score = team_b_score+":"+team_a_score+"|1";
			$(loc_a).text(a_score)
			$(loc_a).css({'font-weight':'bold','text-align':'center','color':'red'})
			$(loc_b).text(b_score)
			$(loc_b).css({'font-weight':'bold','text-align':'center'})

		} else {
			a_score = team_a_score+":"+team_b_score+"|1";
			b_score = team_b_score+":"+team_a_score+"|2";
			$(loc_a).text(a_score)
			$(loc_a).css({'font-weight':'bold','text-align':'center'})
			$(loc_b).text(b_score)
			$(loc_b).css({'font-weight':'bold','text-align':'center','color':'red'})
		};
	}
	cal_credit();
}

function group_sort(c,s) {
	var items = Object.keys(c).map(function(key) {
		  return [key, c[key]];
	});
	// Sort the array based on the second element
	items.sort(function(first, second) {
		  return second[1] - first[1];
	});

	return items
}

function cal_credit(){
	var patt = /\d*\:\d*/;
	var t_ids = []
	var tables =  $('table')
	for(var i=0;i<tables.length;i++){
		if (tables[i].id !=''){
			t_ids.push(tables[i].id)
		}
	}
	var scores = {}
	var credits = {}
	for(var i in t_ids){
		var j = 0;
		var temp = t_ids[i];
		scores[temp] = {}
		credits[temp] = {}
		$('#'+t_ids[i]+' tbody tr').each(function(){
			scores[temp][(j+1)] = [];
			credit = 0;
			$(this).children('td').each(function(){
				if (patt.test($(this).text())){
					//console.log($(this).text())
					scores[temp][(j+1)].push($(this).text().split('|')[0]);
					credit += parseInt($(this).text().split('|')[1])
				}
			})
			credits[temp][(j+1)] = credit;
			$(this).children('td').eq(-2).text(credit);
			$(this).children('td').eq(-2).css({'text-align':'center'});
			j++;
		})						
	}
	credits['league_info'] = $('#league_info').val();
	console.log(credits);
	$.ajax({
		url:'update_credit',
		type:'POST',
		data: {'data':JSON.stringify(credits)},
	})
}