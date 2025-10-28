from django.forms import Form, DateField, CharField, IntegerField
from django.core.exceptions import ValidationError
from django.core import validators

class BasicForm(Form):
    title = CharField(validators = [ validators.MinLengthValidator(2, "Please Enter two or more characters")])
    millage = IntegerField()
    purchase_date = DateField()



from django.forms import ModelForm
from form.models import Cat

# Create the form class.
class CatForm(ModelForm):
    class Meta:
        model = Cat
        # fields = ['name', 'breed', 'comments']
        fields = '__all__'


# References 

# https://docs.djangoproject.com/en/4.2/ref/forms/api/
# https://docs.djangoproject.com/en/4.2/ref/forms/fields/#datefield
# https://docs.djangoproject.com/en/4.2/ref/forms/validation/#using-validation-in-practice
# https://docs.djangoproject.com/en/4.2/ref/validators/
