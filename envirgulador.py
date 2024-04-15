def envirgular(compras):
  tamanho = len(compras)
  i = 0
  while i < tamanho-2:
    if i == 0:
      print(compras[tamanho-tamanho+i], end = '')
      
    print(', '+ compras[tamanho-tamanho+i+1], end = '')
    i = i + 1
    
  print(' and '+ compras[tamanho-1])

listaCompras = ['Macarrão', 'abacate', 'limão', 'goiabada', 'beringela']

envirgular(listaCompras)
