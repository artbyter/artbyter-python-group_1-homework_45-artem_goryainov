from django.views.generic import DetailView, CreateView, UpdateView, View, DeleteView, ListView
from django.urls import reverse
from django.http import HttpResponseRedirect
from webapp.models import Food, Order, OrderFood
from webapp.forms import FoodForm, OrderForm, OrderFoodForm, OrderCourierForm


class FoodListView(ListView):
    model = Food
    template_name = 'food_list.html'


class FoodCreateView(CreateView):
    model = Food
    template_name = 'food_create.html'
    form_class = FoodForm

    def get_success_url(self):
        return reverse('food_detail', kwargs={'pk': self.object.pk})


class FoodUpdateView(UpdateView):
    model = Food
    template_name = 'food_edit.html'
    form_class = FoodForm

    def get_success_url(self):
        return reverse('food_detail', kwargs={'pk': self.object.pk})


class FoodDeleteView(DeleteView):
    model = Food
    template_name = 'food_delete.html'

    def get_success_url(self):
        return reverse('food_create', kwargs={})


class FoodDetailView(DetailView):
    model = Food
    template_name = 'food_detail.html'


class OrdersListView(ListView):
    model = Order
    template_name = 'index.html'


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'


class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'order_update.html'
    form_class = OrderForm

    def get_success_url(self):
        return reverse('order_detail', kwargs={'pk': self.object.pk})


class OrderCourierUpdateView(UpdateView):
    model = Order
    template_name = 'order_update.html'
    form_class = OrderCourierForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courier'] = True
        return context

    def get_success_url(self):
        return reverse('order_detail', kwargs={'pk': self.object.pk})



class OrderRejectViewV2(DeleteView):
    model = OrderUpdateView
    template_name = 'order_cancel.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        # поменять статус на canceled
        # сохранить заказ
        return HttpResponseRedirect(success_url)


# Представления для создания заказа
class OrderCreateView(CreateView):
    model = Order
    template_name = 'order_create.html'
    form_class = OrderForm

    def get_success_url(self):
        return reverse('order_detail', kwargs={'pk': self.object.pk})


# ... и для добавления блюд в заказ
class OrderFoodCreateView(CreateView):
    model = OrderFood
    form_class = OrderFoodForm
    template_name = 'order_food_create.html'

    def get_success_url(self):
        return reverse('order_detail', kwargs={'pk': self.object.order.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_pk'] = self.kwargs.get('pk')
        return context

    def form_valid(self, form):
        form.instance.order = Order.objects.get(pk=self.kwargs.get('pk'))
        return super().form_valid(form)




class OrderFoodDeleteView(DeleteView):


    model = OrderFood
    template_name = 'order_food_delete.html'

    def get_success_url(self):
        return reverse('order_detail', kwargs={'pk': self.object.order.pk})
