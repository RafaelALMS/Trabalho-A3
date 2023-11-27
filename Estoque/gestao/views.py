from django.shortcuts import render , redirect
from django.http import HttpResponse
from .forms import AD_Funci, AD_Estoque
from gestao.models import Funci, estoque

# Create your views here.


def Hellowold(requeste):
    return HttpResponse("hola filha da puta")


def crud(request):#Mostra todos os Produtos

    listaEstoque= estoque.objects.all()#mostra todo o estoque

    context={'request':request,'listaEstoque' : listaEstoque }
    return render(request,'CRUD.html',context)



def add_Funci(request):#Cria Funcionarios
    lista_Funci= Funci.objects.all()#Pega todos os tados dos funcionarios

    form= AD_Funci()



    if request.method == 'POST':
        print(request.POST)
        form= AD_Funci(request.POST)
        if form.is_valid():
            form.save()
 
    

    context=context={'request':request, 'lista_Funci':lista_Funci, 'form':form}
    return render(request,'addFunci.html',context)

def add_Estoque(request):#Coloca produtos no estoque
    lista_estoque= estoque.objects.all()#pega todos os itens do estoque
    form=AD_Estoque()
    if request.method=="POST":
        form=AD_Estoque(request.POST)
        if form.is_valid:
            form.save()
    

    context=context={'request':request, 'lista_estoque':lista_estoque, 'form':form}
    return render(request,'addestoque.html',context)


def update(request, pk):
    data={}
    update_estoque= estoque.objects.get(idSto=pk)
    form = AD_Estoque(request.POST or None,instance=update_estoque)
    
    if form.is_valid():
            form.save()
            return redirect('Adcionar_Estoque/')


    data['form']=form
    context=context={'request':request, 'form':form,'data':data}             
    return render(request,'addestoque.html',context)