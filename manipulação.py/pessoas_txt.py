def cadastrar_pessoa():
    print("cadastro de pessoas ") 
    nome = input("digite o nome ")
    email = input("digite o e-mail: ")

    open("pessoa.txt", "a", escoding="utf-8") 
    arquivo.write(f"{nome},{email}\n") # type: ignore

    print("dados cadastrado com sucesso!")