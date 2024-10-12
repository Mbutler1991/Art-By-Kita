from home.sitemaps import HomeSitemap
from gallery.sitemaps import PaintingSitemap
from orders.sitemaps import OrdersSitemap    
from contact.sitemaps import ContactSitemap    

sitemaps = {
    'home': HomeSitemap,
    'gallery': PaintingSitemap,
    'orders': OrdersSitemap,     
    'contact': ContactSitemap,    
}