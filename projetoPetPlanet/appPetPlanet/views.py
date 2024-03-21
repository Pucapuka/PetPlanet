from django.shortcuts import render
from .models import Cliente
from .models import Pet
from .models import Funcionario
from .gerarPet import gerarDadosPet
from .gerarPessoa import gerarDadosCliente
import sqlite3
import random


# Função temporária, para debug
def limparBD(request):
    bd = sqlite3.connect('db.sqlite3')
    cursor = bd.cursor()
    cursor.execute(
        'DELETE from appPetPlanet_cliente WHERE id_cliente>1')
    bd.commit()
    bd.close()
    return render(request, 'home.html')


def home(request):
    return render(request, 'home.html')

# FUNÇÕES CLIENTE


def cadastrarCliente(request):
    return render(request, 'cliente/cadastrarCliente.html')


def preencherDadosCliente(request):
    args = gerarDadosCliente()
    return render(request, 'cliente/cadastrarCliente.html', args)


def salvarNovoClienteNoBD(request):
    cliente = Cliente()
    cliente.nome = request.POST.get('nome')
    cliente.cpf = request.POST.get('cpf')
    cliente.email = request.POST.get('email')
    cliente.telefone = request.POST.get('telefone')
    cliente.endereco = request.POST.get('endereco')
    cliente.save()
    return render(request, 'cliente/cadastrarCliente.html')


def excluirClienteDoBD(request, IDCliente):
    bd = sqlite3.connect('db.sqlite3')
    cursor = bd.cursor()
    cursor.execute(
        'DELETE from appPetPlanet_cliente WHERE id_cliente='+str(IDCliente))
    bd.commit()
    bd.close()
    clientes = {
        'clientes': Cliente.objects.all()
    }
    return render(request, 'cliente/listarClientes.html', clientes)


def editarClienteNoDB(request, IDCliente):
    cliente = Cliente()
    cliente.nome = request.POST.get('nome')
    cliente.cpf = request.POST.get('cpf')
    cliente.email = request.POST.get('email')
    cliente.telefone = request.POST.get('telefone')
    cliente.endereco = request.POST.get('endereco')

    bd = sqlite3.connect('db.sqlite3')
    cursor = bd.cursor()
    cursor.execute("UPDATE appPetPlanet_cliente SET nome='" +
                   str(cliente.nome) + "' WHERE id_cliente=" + str(IDCliente))
    cursor.execute("UPDATE appPetPlanet_cliente SET cpf='" +
                   str(cliente.cpf) + "' WHERE id_cliente=" + str(IDCliente))
    cursor.execute("UPDATE appPetPlanet_cliente SET email='" +
                   str(cliente.email) + "' WHERE id_cliente=" + str(IDCliente))
    cursor.execute("UPDATE appPetPlanet_cliente SET telefone='" +
                   str(cliente.telefone) + "' WHERE id_cliente=" + str(IDCliente))
    cursor.execute("UPDATE appPetPlanet_cliente SET endereco='" +
                   str(cliente.endereco) + "' WHERE id_cliente=" + str(IDCliente))
    bd.commit()
    bd.close()

    clientes = {
        'clientes': Cliente.objects.all()
    }
    return render(request, 'cliente/listarClientes.html', clientes)


def listarClientes(request):
    clientes = {
        'clientes': Cliente.objects.all()
    }
    return render(request, 'cliente/listarClientes.html', clientes)


def infoCliente(request, IDCliente):
    cliente = Cliente.objects.get(id_cliente=IDCliente)
    pets = Pet.objects.filter(id_dono=IDCliente)
    args = {
        'cliente': cliente,
        'pets': pets,
    }
    return render(request, 'cliente/infoCliente.html', args)

# FUNÇÕES DO PET


def cadastrarPet(request):
    clientes = {
        'clientes': Cliente.objects.all()
    }
    return render(request, 'pet/cadastrarPet.html', clientes)


def salvarNovoPetNoBD(request):
    pet = Pet()
    pet.nome = request.POST.get('nome')
    pet.especie = request.POST.get('especie')
    pet.raca = request.POST.get('raca')
    pet.idade = request.POST.get('idade')
    pet.sexo = request.POST.get('sexo')
    pet.porte = request.POST.get('porte')
    pet.alergias = request.POST.get('alergias')
    pet.id_dono = request.POST.get('dono')
    pet.save()
    return render(request, 'pet/cadastrarPet.html')


def listarPets(request):
    pets = {
        'pets': Pet.objects.all()
    }
    return render(request, 'pet/listarPets.html', pets)


def infoPet(request, IDPet):
    pet = Pet.objects.get(id_pet=IDPet)
    try:
        dono = Cliente.objects.get(id_cliente=pet.id_dono)
    except Cliente.DoesNotExist:
        dono = Cliente()
        dono.nome = "Sem dono definido"
    args = {
        'pet': pet,
        'dono': dono,
        'clientes': Cliente.objects.all(),
    }
    return render(request, 'pet/infoPet.html', args)


def excluirPetDB(request, IDPet):
    bd = sqlite3.connect('db.sqlite3')
    cursor = bd.cursor()
    cursor.execute(
        'DELETE from appPetPlanet_pet WHERE id_pet='+str(IDPet))
    bd.commit()
    bd.close()
    pets = {
        'pets': Pet.objects.all()
    }
    return render(request, 'pet/listarPets.html', pets)


def editarPetNoDB(request, IDPet):
    pet = Pet()
    pet.nome = request.POST.get('nome')
    pet.especie = request.POST.get('especie')
    pet.raca = request.POST.get('raca')
    pet.idade = request.POST.get('idade')
    pet.sexo = request.POST.get('sexo')
    pet.porte = request.POST.get('porte')
    pet.alergias = request.POST.get('alergias')
    pet.id_dono = request.POST.get('dono')

    bd = sqlite3.connect('db.sqlite3')
    cursor = bd.cursor()
    cursor.execute("UPDATE appPetPlanet_pet SET nome='" +
                   str(pet.nome) + "' WHERE id_pet=" + str(IDPet))
    cursor.execute("UPDATE appPetPlanet_pet SET especie='" +
                   str(pet.especie) + "' WHERE id_pet=" + str(IDPet))
    cursor.execute("UPDATE appPetPlanet_pet SET raca='" +
                   str(pet.raca) + "' WHERE id_pet=" + str(IDPet))
    cursor.execute("UPDATE appPetPlanet_pet SET idade='" +
                   str(pet.idade) + "' WHERE id_pet=" + str(IDPet))
    cursor.execute("UPDATE appPetPlanet_pet SET sexo='" +
                   str(pet.sexo) + "' WHERE id_pet=" + str(IDPet))
    cursor.execute("UPDATE appPetPlanet_pet SET porte='" +
                   str(pet.porte) + "' WHERE id_pet=" + str(IDPet))
    cursor.execute("UPDATE appPetPlanet_pet SET alergias='" +
                   str(pet.alergias) + "' WHERE id_pet=" + str(IDPet))
    cursor.execute("UPDATE appPetPlanet_pet SET id_dono='" +
                   str(pet.id_dono) + "' WHERE id_pet=" + str(IDPet))

    bd.commit()
    bd.close()

    pets = {
        'pets': Pet.objects.all()
    }
    return render(request, 'pet/listarPets.html', pets)


def preencherDadosPet(request):
    args = gerarDadosPet()
    args.update({'clientes': Cliente.objects.all()})
    return render(request, 'pet/cadastrarPet.html', args)

# FUNÇÕES DO FUNCIONÁRIO


def cadastrarFuncionario(request):
    return render(request, 'funcionario/cadastrarFuncionario.html')


def salvarNovoFuncionarioNoDB(request):
    funcionario = Funcionario()
    funcionario.nome = request.POST.get('nome')
    funcionario.cpf = request.POST.get('cpf')
    funcionario.email = request.POST.get('email')
    funcionario.telefone = request.POST.get('telefone')
    funcionario.endereco = request.POST.get('endereco')
    funcionario.salario = request.POST.get('salario')
    funcionario.cargo = request.POST.get('cargo')
    funcionario.save()
    return render(request, 'funcionario/cadastrarFuncionario.html')


def listarFuncionarios(request):
    funcionarios = {
        'funcionarios': Funcionario.objects.all()
    }
    return render(request, 'funcionario/listarFuncionarios.html', funcionarios)


def preencherDadosFuncionario(request):
    args = gerarDadosCliente()
    args.update({'cargo': random.choice(["Groomer", "Atendente de Loja", "Veterinário", "Banho e Tosa", "Recepcionista",
                "Esteticista Animal", "Auxiliar de Veterinária", "Faz o cafézinho", "Auxiliar de Banho e Tosa"])})
    args.update({'salario': random.randint(1412, 3000)})
    return render(request, 'funcionario/cadastrarFuncionario.html', args)


def infoFuncionario(request, IDFuncionario):
    args = {
        'funcionario': Funcionario.objects.get(id_funcionario=IDFuncionario),
    }
    return render(request, 'funcionario/infoFuncionario.html', args)


def excluirFuncionarioDoDB(request, IDFuncionario):
    bd = sqlite3.connect('db.sqlite3')
    cursor = bd.cursor()
    cursor.execute(
        'DELETE from appPetPlanet_funcionario WHERE id_funcionario='+str(IDFuncionario))
    bd.commit()
    bd.close()
    funcionarios = {
        'funcuionarios': Funcionario.objects.all()
    }
    return render(request, 'funcionario/listarFuncionarios.html', funcionarios)


def editarFuncionarioNoDB(request, IDFuncionario):
    funcionario = Funcionario()
    funcionario.nome = request.POST.get('nome')
    funcionario.cpf = request.POST.get('cpf')
    funcionario.email = request.POST.get('email')
    funcionario.telefone = request.POST.get('telefone')
    funcionario.endereco = request.POST.get('endereco')
    funcionario.salario = request.POST.get('salario')
    funcionario.cargo = request.POST.get('cargo')

    bd = sqlite3.connect('db.sqlite3')
    cursor = bd.cursor()
    cursor.execute("UPDATE appPetPlanet_funcionario SET nome='" +
                   str(funcionario.nome) + "' WHERE id_funcionario=" + str(IDFuncionario))
    cursor.execute("UPDATE appPetPlanet_funcionario SET cpf='" +
                   str(funcionario.cpf) + "' WHERE id_funcionario=" + str(IDFuncionario))
    cursor.execute("UPDATE appPetPlanet_funcionario SET email='" +
                   str(funcionario.email) + "' WHERE id_funcionario=" + str(IDFuncionario))
    cursor.execute("UPDATE appPetPlanet_funcionario SET telefone='" +
                   str(funcionario.telefone) + "' WHERE id_funcionario=" + str(IDFuncionario))
    cursor.execute("UPDATE appPetPlanet_funcionario SET endereco='" +
                   str(funcionario.endereco) + "' WHERE id_funcionario=" + str(IDFuncionario))
    cursor.execute("UPDATE appPetPlanet_funcionario SET salario='" +
                   str(funcionario.salario) + "' WHERE id_funcionario=" + str(IDFuncionario))
    cursor.execute("UPDATE appPetPlanet_funcionario SET cargo='" +
                   str(funcionario.cargo) + "' WHERE id_funcionario=" + str(IDFuncionario))
    bd.commit()
    bd.close()

    funcionarios = {
        'funcionarios': Funcionario.objects.all()
    }
    return render(request, 'funcionario/listarFuncionarios.html', funcionarios)
