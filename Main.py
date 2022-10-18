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

grafico.set_title('Vendidos vs Devolvidos')

plt.savefig("VendidosXDevolvidos.png")
plt.show()

#Qual/Quais a/s obra/s mais vendida?

print(df.nlargest(10,"TOTAL DE COPIAS")[["TITULO ORIGINAL","TOTAL DE COPIAS"]])

#Vendas por mês.

total_vendas_mes = df.loc[df["MOVIMENTO"] == "VENDA"].groupby("MES")["TOTAL DE COPIAS"].sum().unique()
mes = df["MES"].sort_values().unique()
plt.style.use("classic")
fig1, grafico = plt.subplots()
grafico.bar(mes,total_vendas_mes, label = mes)

grafico.set_ylabel('Total de vendas')
grafico.set_xlabel('Mês')
grafico.set_title('Vendas do ano de 2021')

plt.savefig("Vendas_do_ano_de_2021.png")
plt.show()


#Escreve o novo conjunto de dados
df.to_excel("Tabela_de_Amostras.xlsx", index = False)


