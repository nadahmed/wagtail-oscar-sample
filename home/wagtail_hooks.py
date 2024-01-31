from django.urls import reverse

from wagtail import hooks
from wagtail.admin.menu import MenuItem

@hooks.register('register_admin_menu_item')
def register_shop_dashboard_menu_item():
  return MenuItem('Shop Dashboard', reverse("dashboard:index"), icon_name='link-external', order=0, attrs={'target': '_blank'})