altura = float(input("Digite a Altura em centimetros: ")) #Pede os dados de altura para a cubagem, em centimetros
comprimento = float(input("Digite o Comprimento em centimetros: ")) #Pede os dados de comprimento para a cubagem, em centimetros
largura = float(input("Digite a Largura em centimetros: ")) #Pede os dados de largura para a cubagem, em centimetros

cubagem = altura*comprimento*largura/1000000 #Faz a cubagem e a divide por 1 milhão, para ter a centena da cubagem (0,100, 0,250, etc)

print(cubagem) #Envia o valor da cubagem
