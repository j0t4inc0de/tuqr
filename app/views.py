from django.shortcuts import render, HttpResponse
import qrcode
import os

def inicio(request):
    return render(request, 'masterTemplate.html')

def procesar_datos(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        
        print(f"Link: {link}")
        
        dataLink = link

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(dataLink)
        qr.make(fit=True)
        ruta_guardado = os.path.join('static', 'img', f"miqr.png")

        img = qr.make_image(fill_color="black", back_color="white")
        img.save(ruta_guardado)
        return render(request, 'imagen_generada.html', {'ruta_imagen': ruta_guardado})