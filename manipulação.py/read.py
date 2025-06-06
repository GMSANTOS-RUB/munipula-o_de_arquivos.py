arquivo = open('arquivo.txt', 'r', encoding='utf-8')
# leitura de arquivo
conteudo = arquivo.read()
# imprimir o conteudo do arquivo
print(conteudo)
# fechar o arquivo
arquivo.close()