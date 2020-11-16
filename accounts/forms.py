from django.forms import ModelForm
from .models import *
# from .models import Customer
# from .models import Product

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'



class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'

class CategoryForm(ModelForm):
	class Meta:
		model = Category 
		fields='__all__'


class ProductForm(ModelForm):
	class Meta:
		model = Product	
		fields = '__all__'	


class BrandForm(ModelForm):
	class Meta:
		model = Brand 
		fields =['name']

		def clean_brand_name(self):
			name = self.cleaned_data.get('name')
			for instance in Brand.object.all():
				if instance.name==name:
					raise forms.ValidationError(name,'Already Exists')
			return name 
class ExpenseForm(ModelForm):
	class Meta:
		model=Expense
		fields='__all__'

class AppConfigForm(ModelForm):
	class Meta:
		model=AppConfig
		fields='__all__'