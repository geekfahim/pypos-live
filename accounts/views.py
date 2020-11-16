from django.shortcuts import render, redirect
from django.core import serializers
from django.http import JsonResponse

from django.http import HttpResponse
from django.db.models import Avg, Count, Min, Sum
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

def createProduct(request):
	form = ProductForm()
	if request.method=='POST':
		form = ProductForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('products')
	context={'form':form}		
	return render(request,'accounts/product_form.html',context)

def updateProduct(request,pk):
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


def customerPage(request,pk):
	customer = Customer.objects.get(id=pk)
	orders = customer.order_set.all()
	total_order = orders.count()
	context = {'customer':customer,'orders':orders,'total_order':total_order}
	return render(request,'accounts/customerdetails.html',context)

def customerAj(request):
	if request.is_ajax and request.method=="POST":
		name=request.POST['name']
		phone=request.POST['phone']
		email=request.POST['email']
		address=request.POST['address']

		Customer.objects.create(
			name=name,
			phone=phone,
			email=email,
			address=address
		)
	return HttpResponse('oks')	
    # # request should be ajax and method should be POST.
    # if request.is_ajax and request.method == "POST":
    #     # get the form data
    #     form = CustomerForm(request.POST)
    #     # save the data and after fetch the object in instance
    #     if form.is_valid():
    #         instance = form.save()
    #         # serialize in new friend object in json
    #         ser_instance = serializers.serialize('json', [ instance, ])
    #         # send to client side.
    #         return JsonResponse({"instance": ser_instance}, status=200)
    #     else:
    #         # some form errors occured.
    #         return JsonResponse({"error": form.errors}, status=400)

    # # some error occured
    # return JsonResponse({"error": ""}, status=400)

def createCustomer(request):
	form = CustomerForm()
	if request.method == 'POST':
		# print('saa'request.POST)
		form = CustomerForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('customer')
	context = {'form':form}			
	return render(request,'accounts/customer_form.html',context)


def updateCustomer(request,pk):
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
				return redirect('order')

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
	currency=AppConfig.objects.all()
	expense=Expense.objects.all()
	context={'expense':expense,'currency':currency}
	return render(request,'accounts/expense.html',context)

def createExpense(request):
	form=ExpenseForm()
	if request.method=='POST':
		form=ExpenseForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('expense')
	context={'form':form}			
	return render(request,'accounts/expense_form.html',context)


def updateExpense(request,pk):
	expense=Expense.objects.get(id=pk)
	form=ExpenseForm(instance=expense)
	if request.method=='POST':
		form=ExpenseForm(request.POST,instance=expense)
		if form.is_valid():
			form.save()
			return redirect('expense')
	context={'form':form}
	return render(request,'accounts/expense_form.html',context)			


def appConfigUpdate(request,pk):
	appconfig=AppConfig.objects.filter(app_name=pk)	
	form=AppConfigForm()
	if request.method=='POST':
		form = AppConfigForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('accounts/settings')
	context={'form':form}
	return render(request,'accounts/settings.html',context)
