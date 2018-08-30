from django.forms import ModelForm, ValidationError
from .models import *

class GameSessionSubmissionForm(ModelForm):

	def forecast_submissions(self):
		#are all forecasts & order not null, and >0
		pass

	def period(self):
		#is period submission still current period
		pass

	class Meta:
		model=GameSessionSubmission

class GameParameterSettingsForm(ModelForm):

    # def clean_age(self):
    #     """Validate age to make sure that the person is at least 21 years old"""
    #     age = self.cleaned_data['age']
    #     if age < 21 or age > 130:
    #         raise ValidationError("")
    #     return age

    # def saveWithBar(self, bar, commit=True):
    #     checkin = CheckIn(
    #         isMale=self.cleaned_data['isMale'],
    #         age=self.cleaned_data['age'],
    #         bar=bar,
    #         created_at=Bar.now())
    #     if commit:
    #         checkin.save()
    #     return checkin

    class Meta:
        model = GameParameterSettings


class CommentLogForm(ModelForm):
    def saveComment(self, commentLog, commit=True):
        pass

    class Meta:
        model = CommentLog

class GameSettingsForm(ModelForm):
	class Meta:
		model = GameSettings

class VisibilityGameSettingsForm(ModelForm):

	class Meta:
		model = VisibilityGameSettings
