from django.urls import reverse

from wagtail import hooks
from wagtail.admin.menu import MenuItem

@hooks.register('register_admin_menu_item')
def register_shop_dashboard_menu_item():
  return MenuItem('Shop Dashboard', reverse("dashboard:index"), icon_name='link-external', order=0, attrs={'target': '_blank'})

class UserbarShopLinkItem:
    def render(self, request):
        from django.template import Template, Context
        doc = '''
        <li class="wagtail-userbar__item " role="presentation">
          <a href="{% url 'dashboard:index' %}" target="_blank" role="menuitem" tabindex="-1">
            <svg class="icon icon-link-external wagtail-action-icon" aria-hidden="true">
            {% include "wagtailadmin/icons/link-external.svg" %}</svg>
                Go to Shop Dashboard
          </a>
        </li>
        '''
        t = Template(doc)
        return t.render(Context({}))

@hooks.register('construct_wagtail_userbar')
def add_shop_dashboard_link_item(request, items:list=[]):
    items.insert(1, UserbarShopLinkItem())
    return items