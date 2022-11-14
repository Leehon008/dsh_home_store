import time
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Products
from store.models.orders import Order
from paynow import Paynow


class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Products.get_products_by_id(list(cart.keys()))
      #  print(address, phone, customer, cart, products)

        paynow = Paynow(
            '15451', 
            '74f7d1fa-cff6-44af-8356-ffc78d04fbeb',
            'http://google.com', 
            'http://google.com'
            )

        payment = paynow.create_payment('Order', 'honye.lewism@gmail.com')

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
            payment.add(product.name, product.price)
        print(payment.info)
        # response = paynow.send_mobile(payment, '0785149408', 'ecocash')
        response =  paynow.send(payment)

        if(response.success):
            poll_url = response.poll_url
            print("Poll Url: ", poll_url)
            status = paynow.check_transaction_status(poll_url)
            time.sleep(30)
            print("Payment Status: ", status.status)
        request.session['cart'] = {}

        return redirect('cart')
