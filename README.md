# Analise Exploratoria - Ancine
## Objetivo Geral
- Praticar o uso da biblioteca Pandas;
- Analisar a distribuição de vídeos em âmbito doméstico;

## INTRODUÇÃO

Segundo a IBM a EDA - análise exploratória de dados, é usada comumente por cientistas de dados para investigar e analisar uma série de dados e expor as principais características. Como objeto de estudo, este relatório traz uma breve análise dos dados públicos da ANCINE - Agência Nacional do Cinema, a respeito da [distribuição de vídeos domésticos](https://dados.gov.br/dataset/relatorio-de-distribuicao-de-obras-de-video-domestico-por-mes/resource/c9b830ef-026f-4da9-9d96-b73f68b08004) do ano de 2021, com a finalidade de praticar a biblioteca Pandas do Python. 

## ANÁLISE

### Remoção 

O arquivo [.csv original](https://dados.gov.br/dataset/relatorio-de-distribuicao-de-obras-de-video-domestico-por-mes/resource/c9b830ef-026f-4da9-9d96-b73f68b08004) possui 1.265.342 linhas e 16 colunas, com um tamanho de 221.511 KB. Após a limpeza dos dados que não seriam utilizados nas análise, foi gerado um [arquivo final](https://github.com/Pedro-Alvess/Analise-Exploratoria-Ancine/blob/main/Tabela_de_Amostras.xlsx) com 4.052 linhas e 10 colunas, com um tamanho de 203 KB.

```
#Remoção de todos os anos anteriores a 2021
anos_anteriores = df.loc[df["ANO"] != 2021].index
df.drop(anos_anteriores, inplace=True)
```
```
#Remoção das colunas que não fazem parte da análise
df.drop(["REGISTRO_DISTRIBUIDORA", "CNPJ_DISTRIBUIDORA","CPB_ROE","ID_PACOTE","NOME_PACOTE","NR_TITULOS_PACOTE"], axis=1, inplace= True)
```
```
#Remoção de linhas com o titulo em branco
df.dropna(subset=["TITULO_ORIGINAL"], inplace=True)
```
### Edição 

A fim de adequar todos os títulos das colunas remanescentes, foi removido e resumidos os títulos originais, como por exemplo "RAZAO_SOCIAL_DISTRIBUIDORA" passou a ser "DISTRIBUIDORA". 

```
#Edição dos nomes das colunas
df = df.rename(columns={"RAZAO_SOCIAL_DISTRIBUIDORA":"DISTRIBUIDORA","TITULO_ORIGINAL":"TITULO ORIGINAL", "TITULO_BRASILEIRO":"TITULO BRASILEIRO",
                        "PAIS_OBRA":"PAIS DE ORIGEM","MODALIDADE_VENDAS":"MODALIDADE DE VENDAS","TIPO_SUPORTE":"TIPO DE SUPORTE", "NR_COPIAS":"TOTAL DE COPIAS"})
```

### Análise

- Qual a proporção entre vendidos e devolvidos? 

Resultado gerado:

![VendidosXDevolvidos](/Graficos/VendidosXDevolvidos.png)

O código que gerou este resultado foi:
```
#Qual a proporção entre vendidos e devolvidos?


labels = df["MOVIMENTO"].unique()
sizes = df["MOVIMENTO"].value_counts()
plt.style.use("classic")
fig1, grafico = plt.subplots()
grafico.pie(sizes, labels=labels, autopct='%1.1f%%', colors=("limegreen","cornflowerblue"))

grafico.set_title('Vendidos vs Devolvidos')

plt.savefig("VendidosXDevolvidos.png")
plt.show()

```

- Qual/Quais a/s obra/s mais vendida?

O primeiro valor informado é o indice, depois o Titulo original e o total de copias.

Resultado gerado:

```
                                 TITULO ORIGINAL  TOTAL DE COPIAS
469051              ZACK SNYDER'S JUSTICE LEAGUE             5960
801898  HARRY POTTER AND THE PHILOSOPHER'S STONE             3556
136597  HARRY POTTER AND THE PHILOSOPHER'S STONE             3241
821697                    CHERNOBYL FIRST SEASON             3000
821695                         WONDER WOMAN 1984             2666
19542   HARRY POTTER AND THE PHILOSOPHER'S STONE             2536
684689                               VIDAS SÊCAS             2001
254504                                BLACK SWAN             2000
605867                                    AVATAR             2000
605868                                  I, ROBOT             2000
```

O código que gerou este resultado foi:

```
#Qual/Quais a/s obra/s mais vendida?

print(df.nlargest(10,"TOTAL DE COPIAS")[["TITULO ORIGINAL","TOTAL DE COPIAS"]]
```

- Vendas por mês.

Resultado gerado:

![Vendas_do_ano_de_2021](/Graficos/Vendas_do_ano_de_2021.png)

O código que gerou este resultado foi:
```
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
```
