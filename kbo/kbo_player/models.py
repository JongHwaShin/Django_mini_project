from django.db import models
from django.utils import timezone

# Create your models here.
picher = '투수'
batter = '타자'
team_dict = {'nc':'NC','doosan':'두산','kia':'KIA','kt':'KT','hanhwa':'한화','lg':'LG','ssg':'SSG','lotte':'롯데','kiwoom':'키움'}
position_choices = [(picher,'투수'),(batter,'타자')]
#앞에 값이 화면에 출력되는 값!
team_choices = [('nc',team_dict['nc']),('doosan',team_dict['doosan']),('kia',team_dict['kia']),('kt',team_dict['kt']),('hanhwa',team_dict['hanhwa']),
                    ('lg',team_dict['lg']),('ssg',team_dict['ssg']),('lotte',team_dict['lotte']),('kiwoom',team_dict['kiwoom'])]

class Kboplayer(models.Model):
    name = models.CharField(max_length=100) #선수이름
    team = models.CharField(max_length=10,choices=team_choices,default=None) #소속팀명
    position = models.CharField(max_length=5,choices=position_choices,default=None) #포지션
    year_money = models.CharField(max_length=1000,null=True)
    year = models.CharField(max_length=100,null=True)
    created_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(blank=True,null=True)
    attack_or_attacked = models.CharField(max_length=100,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.name + '(' + self.year + ')'

class Comment(models.Model):
    player_post = models.ForeignKey('kbo_player.Kboplayer',on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.text

class Player(models.Model):

    순위 = models.TextField(blank=True, null=True)
    선수명 = models.TextField(blank=True,primary_key=True)
    팀명 = models.TextField(blank=True, null=True)
    avg = models.TextField(db_column='AVG', blank=True, null=True)  # Field name made lowercase.
    g = models.TextField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    pa = models.TextField(db_column='PA', blank=True, null=True)  # Field name made lowercase.
    ab = models.TextField(db_column='AB', blank=True, null=True)  # Field name made lowercase.
    r = models.TextField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    h = models.TextField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    number_2b = models.TextField(db_column='2B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    number_3b = models.TextField(db_column='3B', blank=True, null=True)  # Field name made lowercase. Field renamed because it wasn't a valid Python identifier.
    hr = models.TextField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    tb = models.TextField(db_column='TB', blank=True, null=True)  # Field name made lowercase.
    rbi = models.TextField(db_column='RBI', blank=True, null=True)  # Field name made lowercase.
    sac = models.TextField(db_column='SAC', blank=True, null=True)  # Field name made lowercase.
    sf = models.TextField(db_column='SF', blank=True, null=True)  # Field name made lowercase.

class Player2(models.Model):
    순위 = models.TextField(blank=True, null=True)
    선수명 = models.TextField(blank=True, primary_key=True)
    팀명 = models.TextField(blank=True, null=True)
    era = models.TextField(db_column='ERA', blank=True, null=True)  # Field name made lowercase.
    g = models.TextField(db_column='G', blank=True, null=True)  # Field name made lowercase.
    w = models.TextField(db_column='W', blank=True, null=True)  # Field name made lowercase.
    l = models.TextField(db_column='L', blank=True, null=True)  # Field name made lowercase.
    sv = models.TextField(db_column='SV', blank=True, null=True)  # Field name made lowercase.
    hld = models.TextField(db_column='HLD', blank=True, null=True)  # Field name made lowercase.
    wpct = models.TextField(db_column='WPCT', blank=True, null=True)  # Field name made lowercase.
    ip = models.TextField(db_column='IP', blank=True, null=True)  # Field name made lowercase.
    h = models.TextField(db_column='H', blank=True, null=True)  # Field name made lowercase.
    hr = models.TextField(db_column='HR', blank=True, null=True)  # Field name made lowercase.
    bb = models.TextField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
    hbp = models.TextField(db_column='HBP', blank=True, null=True)  # Field name made lowercase.
    so = models.TextField(db_column='SO', blank=True, null=True)  # Field name made lowercase.
    r = models.TextField(db_column='R', blank=True, null=True)  # Field name made lowercase.
    er = models.TextField(db_column='ER', blank=True, null=True)  # Field name made lowercase.
    whip = models.TextField(db_column='WHIP', blank=True, null=True)  # Field name made lowercase.
