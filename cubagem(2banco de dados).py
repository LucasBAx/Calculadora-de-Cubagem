altura = float(input("Digite a Altura em centimetros: ")) #Pede os dados de altura para a cubagem, em centimetros
comprimento = float(input("Digite o Comprimento em centimetros: ")) #Pede os dados de comprimento para a cubagem, em centimetros
largura = float(input("Digite a Largura em centimetros: ")) #Pede os dados de largura para a cubagem, em centimetros

cubagem = altura*comprimento*largura/1000000 #Faz a cubagem e a divide por 1 milhão, para ter a centena da cubagem (0,100, 0,250, etc)

#Os valores da cubagem são transformados em medida, 0.250 é uma caixa pequena, e assim por diante

if cubagem < 0.250: #se o valor da cubagem for menor que 0.250, a caixa será dada como pequena
 tamanho = "pequena"
elif cubagem < 0.500: #se o valor da cubagem for maior que 0.250 e menor que 0.500, a caixa será dada como médio
 tamanho = "médio"
else: #se o valor da cubagem for maior que 0.500, a caixa será dada como grande
 tamanho = "grande"

print("O tamanho da caixa é", tamanho) #Envia uma mensagem dizendo o tamanho da caixa