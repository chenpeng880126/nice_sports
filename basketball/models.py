from django.db import models

class Team(models.Model):
    team_id = models.CharField(max_length=20,unique=True)
    team_name = models.CharField(max_length=100)
    team_nick_name = models.CharField(max_length=20,default="")
    team_company = models.CharField(max_length=100,blank=True)
    team_level = models.CharField(max_length=10,default="同一级别",blank=True)
    team_group = models.CharField(max_length=10,blank=True)
    team_group_no = models.CharField(max_length=10,default="",blank=True)
    team_credit = models.IntegerField(blank=True,null=True,verbose_name='积分')
    team_rank = models.CharField(max_length=2,default="",null=True,blank=True,verbose_name='排名')
    league = models.CharField(max_length=100,default="zjb",blank=True)
    league_year = models.CharField(max_length=10,default="2019",blank=True)
    def __str__(self):
        return "%d" % self.pk

class Game(models.Model):
    game_id = models.CharField(max_length=20,unique=True)
    league = models.CharField(max_length=10,default="",blank=True)
    league_year = models.CharField(max_length=10,default="")
    game_level = models.CharField(max_length=10,blank=True)
    game_group = models.CharField(max_length=10,blank=True)
    game_date = models.DateField(blank=True)
    game_start_time = models.TimeField(blank=True)
    game_end_time = models.TimeField(blank=True)
    game_court = models.CharField(max_length=50,blank=True)
    team_a = models.CharField(max_length=50,default="",blank=True)
    team_a_group_no = models.CharField(max_length=10,default="",verbose_name='Group',blank=True)
    team_a_score = models.IntegerField(blank=True,null=True)
    team_b = models.CharField(max_length=50,default="",blank=True)
    team_b_group_no = models.CharField(max_length=10,default="",verbose_name='Group',blank=True)
    team_b_score = models.IntegerField(blank=True,null=True)
    court_address = models.CharField(max_length=100,blank=True)
    game_complete = models.BooleanField(default=False,blank=True)

    GAME_TYPE = (
        ('r','Regular'),
        ('p','Playoff')
        )
    game_type = models.CharField(max_length=1,choices=GAME_TYPE,default='r')

    def __str__(self):
        return "%d" % self.pk