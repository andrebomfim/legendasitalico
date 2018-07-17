arquivo = input('Insira o nome completo do arquivo: ')
texto = open(arquivo, 'r', encoding='utf8')

novo = ''

print(f'Formatando itálicos de {arquivo}...')
for linha in texto:
    if linha.startswith('<i>') and '</i>' not in linha:
        linha = linha.strip('\n') + '</i>\n'
    elif linha.endswith('</i>\n') and '<i>' not in linha:
        linha = '<i>' + linha
    else:
        pass
    novo += linha

print('Formatação concluída.')
texto.close()

print('Gravando arquivo formatado...')
arquivonovo = arquivo.split('.')[0] + '_formatado.txt'
formatado = open(arquivonovo, 'w', encoding='utf8')
for linha in novo:
    formatado.write(linha)
formatado.close()
print(f'Arquivo {arquivonovo} gravado com sucesso.')
