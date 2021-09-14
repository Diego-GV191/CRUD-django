from django.shortcuts import render, redirect
from .models import Curso

# Create your views here.
def home(request):
	cursos = Curso.objects.all()
	return render(request, 'gestionCursos.html', {
		"cursos": cursos
		})

def registrarCurso(request):
	codigo=request.POST['txtCodigo']
	nombre=request.POST['txtNombre']
	creditos=request.POST['numCredito']

	curso = Curso.objects.create(codigo=codigo, nombre=nombre, credito=creditos)
	return redirect('/')

def edicionCurso(request, codigo):
	curso = Curso.objects.get(codigo=codigo)
	return render(request, 'edicionCurso.html', {
		"curso": curso
		})

def editarCurso(request):
	codigo=request.POST['txtCodigo']
	nombre=request.POST['txtNombre']
	creditos=request.POST['numCredito']

	curso = Curso.objects.get(codigo=codigo)
	curso.nombre = nombre
	curso.credito = creditos
	curso.save()
	
	return redirect('/')

def eliminarCurso(request, codigo):
	curso = Curso.objects.get(codigo=codigo)
	curso.delete()
	return redirect('/')