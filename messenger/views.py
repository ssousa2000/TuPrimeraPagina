from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Mensaje
from .forms import MensajeForm

@login_required
def inbox(request):
    mensajes_recibidos = request.user.mensajes_recibidos.all()
    mensajes_enviados = request.user.mensajes_enviados.all()
    return render(request, 'messenger/inbox.html', {
        'mensajes_recibidos': mensajes_recibidos,
        'mensajes_enviados': mensajes_enviados,
    })

@login_required
def enviar_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.emisor = request.user
            mensaje.save()
            return redirect('inbox')
    else:
        form = MensajeForm()
    return render(request, 'messenger/enviar_mensaje.html', {'form': form})
