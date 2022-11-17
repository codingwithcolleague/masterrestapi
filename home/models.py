from django.db import models

# Create your models here.
class StaudentMaster(models.Model):
    # template = models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100,null=True)
    # details = models.JSONField(blank=True,null=True,default=dict)
    rollno = models.IntegerField(null=True)
    details = models.JSONField(blank=True,null=True,default=list)
    created_by = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'tbl_student_master'