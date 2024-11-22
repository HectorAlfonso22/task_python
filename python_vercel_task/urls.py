from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Página Principal</title>
    </head>
    <body>
        <h1>Bienvenido a la página principal</h1>
        <p>Haz clic en el botón de abajo para visitar el blog:</p>
        <a href="/blog/">
            <button style="padding: 10px 20px; font-size: 16px; cursor: pointer;">Ir al Blog</button>
        </a>
    </body>
    </html>
    """
    return HttpResponse(html_content)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', home, name='home'),
]
