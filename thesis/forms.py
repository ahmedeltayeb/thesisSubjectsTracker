from django.contrib.auth.forms import UserCreationForm
from crispy_forms.layout import Layout , ButtonHolder, Submit
from crispy_forms.helper import FormHelper



class RegisterationForm(UserCreationForm):
	"""docstring for RegisterationForm"""
	def __init__(self, *args , **kwargs):
		super(RegisterationForm, self).__init__(*args , **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout (
			'username',
			'password1',
			'password2',
			ButtonHolder( 
				Submit ('register','Register',css_class = 'btn_primary')
			)
		)

