from django.db import models
from django.utils import timezone

# Create your models here.

class Kboplayer(models.Model):
    picher = '투수'
    batter = '타자'
    team_dict = {'nc':'NC','doosan':'두산','kia':'KIA','kt':'KT','hanhwa':'한화','lg':'LG','ssg':'SSG','lotte':'롯데','kiwoom':'키움'}
    position_choices = [(picher,'투수'),(batter,'타자')]
    #앞에 값이 화면에 출력되는 값!
    team_choices = [('nc',team_dict['nc']),('doosan',team_dict['doosan']),('kia',team_dict['kia']),('kt',team_dict['kt']),('hanhwa',team_dict['hanhwa']),
                    ('lg',team_dict['lg']),('ssg',team_dict['ssg']),('lotte',team_dict['lotte']),('kiwoom',team_dict['kiwoom'])]
    name = models.CharField(max_length=100) #선수이름
    team = models.CharField(max_length=10,choices=team_choices,default=None) #소속팀명
    position = models.CharField(max_length=5,choices=position_choices,default=None) #포지션
    year_money = models.CharField(max_length=1000,null=True)
    created_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(blank=True,null=True)



    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.name
