import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("DistribuicaoVideoDomesticoMensal.csv", sep = ";",encoding="latin-1",low_memory=False)


#Remoção de todos os anos anteriores a 2021
anos_anteriores = df.loc[df["ANO"] != 2021].index
df.drop(anos_anteriores, inplace=True)

#Remoção das colunas que não fazem parte da análise
df.drop(["REGISTRO_DISTRIBUIDORA", "CNPJ_DISTRIBUIDORA","CPB_ROE","ID_PACOTE","NOME_PACOTE","NR_TITULOS_PACOTE"], axis=1, inplace= True)

#Remoção de linhas com o titulo em branco
df.dropna(subset=["TITULO_ORIGINAL"], inplace=True)


#Edição dos nomes das colunas
df = df.rename(columns={"RAZAO_SOCIAL_DISTRIBUIDORA":"DISTRIBUIDORA","TITULO_ORIGINAL":"TITULO ORIGINAL", "TITULO_BRASILEIRO":"TITULO BRASILEIRO",
                        "PAIS_OBRA":"PAIS DE ORIGEM","MODALIDADE_VENDAS":"MODALIDADE DE VENDAS","TIPO_SUPORTE":"TIPO DE SUPORTE", "NR_COPIAS":"TOTAL DE COPIAS"})


#Qual a proporção entre vendidos e devolvidos?


labels = df["MOVIMENTO"].unique()
sizes = df["MOVIMENTO"].value_counts()
plt.style.use("classic")
fig1, grafico = plt.subplots()
grafico.pie(sizes, labels=labels, autopct='%1.1f%%', colors=("limegreen","cornflowerblue"))

plt.savefig("VendidosXDevolvidos.png")
#plt.show()

#Qual/Quais a/s obra/s mais vendida?

print(df.nlargest(10,"TOTAL DE COPIAS")[["TOTAL DE COPIAS","TITULO ORIGINAL"]])

#Vendas por mês.
#Devoluções por mês.
#Quais são os paises de origem tem mais copias vendidas?


#print(df["MOVIMENTO"].describe())
print(df.dtypes)

df.to_excel("Tabela_de_Amostras.xlsx", index = False)


