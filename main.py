#Desafio Ponto do steak  if, elif, else

 ## Criar um programa que dependendo da temperatura em (celsius) do steak ele retorna o ponto de cozimento em português. O usuário deverá fornecer a temperatura.

# temperaturas - cozimento
# 120°F ou 48 °F - rare(selada)
# 130°F ou 54 °F - medium rare( Ao ponto para o mal)
# 140 °F ou 60 °F - medium(Ao ponto)
# 150 °F ou 65 °F - medium well (Ao ponto para o bem)
# 160 °F ou 71 °F - well done (Bem passada)


temp_cels = int(input("Qual a temperatura da carne?"))

if temp_cels < 48:
    print('Cozinhar por mais alguns minutos')

elif temp_cels in range( 48 , 53):
    print("selada")

elif temp_cels in range( 54 , 59):
    print("Ao ponto para o mal")

elif temp_cels in range( 60 , 64):
    print("Ao ponto")

elif temp_cels in range( 65 , 70):
    print("Ao ponto para o bem")

elif temp_cels >=71:
    print("Bem passada")



