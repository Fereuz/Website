from django.shortcuts import render


menu = [
	{
		'href': 'main',
		'name': 'Домой',
	},
	{
		'href': 'products',
		'name': 'Продукты',
	},
	{
		'href': 'contact',
		'name': 'Контакты',
	},
]
	
def main(request):
	title = 'Главная'
	
	content = {
		'title': title,
		'menu': menu,
	}
	
	return render(request, 'mainapp/index.html', content)


def products(request):
	title = 'Продукты'
	
	content = {
		'title': title,
		'menu': menu,
	}
	
	return render(request, 'mainapp/products.html', content)


def contact(request):
	title = 'Контакты'
	
	contacts_list = [
		{
			'sity': 'Москва',
			'phone': '7-123-456-78-90',
			'email': 'email@email.ru',
			'address': 'На окраине',
		},
		{
			'sity': 'Питер',
			'phone': '7-098-765-43-21',
			'email': 'email@email.ru',
			'address': 'В центре',
		},
		{
			'sity': 'Новосибирск',
			'phone': '7-111-222-33-44',
			'email': 'email@email.ru',
			'address': 'В Сибире',
		},
		]
	
	content = {
		'title': title,
		'contacts_list': contacts_list,
		'menu': menu,
	}
	
	return render(request, 'mainapp/contact.html', content)