from django.shortcuts import render

from django.views import View

from ecommerce.models import Category


class BaseView(View):
    template_context = {
        'categories': Category.objects.order_by('title').all()
    }


class Homepage(BaseView):
    def get(self, request):
        # self.template_context['homepage'] = 'Hello World'
        return render(request, 'index.html', self.template_context)


class CategoryWise(BaseView):
    def get(self, request, category_slug):
        return render(request, 'category-wise.html', self.template_context)
