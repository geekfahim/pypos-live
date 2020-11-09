from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import*
from .forms import*


# Create your views here.

def home(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()
	products = Product.objects.all()
	total_order = orders.count()
	pending = orders.filter(status='pending').count()
	delivered = orders.filter(status='delivered').count()
	total_customer = customers.count()
	context = {'orders':orders,'customers':customers,'products':products,'total_order':total_order,'pending':pending,'delivered':delivered,'total_customer':total_customer}

	return render(request,'accounts/dashboard.html',context)


def category(request):
	category = Category.objects.all()
	context={'category':category}
	return render(request,'accounts/category.html',context)

def createCategory(request):
	form = CategoryForm()
	if request.method =='POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('category')

	context={'form':form}
	return render(request,'accounts/category_form.html',context)


def updateCategory(request,pk):
	category=Category.objects.get(id=pk)	
	form= CategoryForm(instance=category)
	if request.method=='POST':
		form = CategoryForm(request.POST,instance=category)
		if form.is_valid():
			form.save()
			return redirect('category')
	context={'form':form}
	return render(request,'accounts/category_form.html',context)




def brand(request):
	brand=Brand.objects.all()
	context={'brand':brand}
	return render(request,'accounts/brand.html',context)

def createBrand(request):
	form = BrandForm()	
	if request.method=='POST':		
		form = BrandForm(request.POST)
		if form.is_valid():
			messages.error(request,"Brand Created Successfully!")
			form.save()
			return redirect('brand')
		else:
			messages.error(request,"Already Exist!")

	context ={'form':form}
	return render(request,'accounts/brand_form.html',context)	

def updateBrand(request,pk):
	brand=Brand.objects.get(id=pk)
	form=BrandForm(instance=brand)
	if request.method=='POST':
		form=BrandForm(request.POST,instance=brand)
		if form.is_valid():
			messages.error(request,"Brand Updated Successfully!")
			form.save()
			return redirect('brand')
		else:
			messages.error(request,"Already Exist!")	
			return redirect('brand')					
	context={'form':form}
	return render(request,'accounts/brand_form.html',context)






def products(request):
	products = Product.objects.all()
	context={'products':products}
	return render(request,'accounts/products.html', context)

def CreateProduct(request):
	form = ProductForm()
	if request.method=='POST':
		form = ProductForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('products')
	context={'form':form}		
	return render(request,'accounts/product_form.html',context)

def UpdateProduct(request,pk):
	product = Product.objects.get(id=pk)
	form = ProductForm(instance=product)
	if request.method=="POST":
		form = ProductForm(request.POST,instance=product)
		if form.is_valid():
			form.save()
			return redirect('products')
	context={'form':form}
	return render(request,'accounts/product_form.html',context)


def customers(request):
	customers = Customer.objects.all()
	context = {'customers':customers}
	return render(request,'accounts/customer.html',context)


def CustomerPage(request,pk):
	customer = Customer.objects.get(id=pk)
	orders = customer.order_set.all()
	total_order = orders.count()
	context = {'customer':customer,'orders':orders,'total_order':total_order}
	return render(request,'accounts/customerdetails.html',context)

def CreateCustomer(request):
	form = CustomerForm()
	if request.method == 'POST':
		# print('saa'request.POST)
		form = CustomerForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('customer')
	context = {'form':form}			
	return render(request,'accounts/customer_form.html',context)


def UpdateCustomer(request,pk):
	customer = Customer.objects.get(id=pk)
	form = CustomerForm(instance=customer)
	if request.method =='POST':
		form = CustomerForm(request.POST,instance=customer)
		if form.is_valid():
			form.save()
			return redirect('customer')

	context={'form':form}
	return render(request,'accounts/customer_form.html',context)

def createOrder(request):
		form = OrderForm()
		if request.method == 'POST':
			# print('Printing POST:',request.POST)
			form = OrderForm(request.POST)
			if form.is_valid():
				form.save()
				return redirect('/')

		context={'form':form}
		return render(request,'accounts/order_form.html',context)	

def updateOrder(request,pk):
	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method =='POST':
		form = OrderForm(request.POST,instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')


	context={'form':form}
	return render(request,'accounts/order_form.html',context)

def deleteOrder(request,pk):
	order = Order.objects.get(id=pk)

	if request.method =='POST':
		order.delete()
		return redirect('/')
	
	context={'item':order}	
	return render(request,'accounts/delete.html',context)


def expense(request):
	expense=Expense.objects.all()
	context={'expense':expense}
	return render(request,'accounts/expense.html',context)


def appConfig(request):
	appconfig=AppConfig.objects.all()
	form=AppConfigForm(instance=appconfig)
	if request.method=='POST':
		form = AppConfigForm(request.POST,instance=appconfig)
		if form.is_valid():
			form.save()
			return redirect('accounts/settings')
	context={'form':form}
	return render(request,'accounts/settings.html',context)
