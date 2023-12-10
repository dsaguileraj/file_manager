from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.gzip import gzip_page

from api.v1.management.services.file_service import FileService
from api.v1.management.handlers.file_handler import FileHandler


@gzip_page
def list_files(request):
    srv = FileService()
    template = "management/file/list.html"
    if request.session.is_empty():
        return HttpResponseRedirect("/auth/login/")
    files = srv.get_all({"user": request.user})
    return render(request, template, {"files": files})


@gzip_page
def edit_file(request, id: int = None):
    srv = FileService()
    template = "management/file/form.html"
    if request.session.is_empty():
        return HttpResponseRedirect("/auth/login/")
    if id:
        method = "PUT"
        file = srv.get_one(id=id)
        form_title = "Editar Archivo"
        button_text = "Actualizar"
    else:
        method = "POST"
        file = srv.get_empty()
        form_title = "Crear Nuevo Archivo"
        button_text = "Crear"
    if request.method == "GET":
        return render(request, template, {
            "method": method,
            "file": file,
            "form_title": form_title,
            "button_text": button_text,
        })
    handler = FileHandler()
    data = request.POST
    if data.get("method") == "POST":
        resp = handler.create(request)
    elif data.get("method") == "PUT":
        resp = handler.update(request, id)
    id = resp.data["id"]
    return HttpResponseRedirect(f"/management/file/edit/{id}")


@gzip_page
def delete_file(request, id: int = None):
    handler = FileHandler()
    handler.delete(request, id)
    return HttpResponseRedirect("/management/file/")
