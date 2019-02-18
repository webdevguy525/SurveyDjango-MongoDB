from django.db import models

class Survey(models.Model):
	survey_title = models.CharField(max_length = 100)
	amount_votes = models.IntegerField(default = 0)

	def __str__(self):
		return self.survey_title

class Question(models.Model):
	survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
	question_txt = models.CharField(max_length = 300)
	question_img = models.ImageField(null = True, blank = True, upload_to='', default = 'check.png')

	def __str__(self):
		return self.question_txt

class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	answer_txt = models.CharField(max_length = 200)
	answer_votes = models.IntegerField(default=0)

	def __str__(self):
		return self.answer_txt
