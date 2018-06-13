# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 13:58:52 2018

@author: Lux
"""

#importações
import pandas as pd
import matplotlib.pyplot as plt
import plotly.plotly as py
import numpy as np
import random 
from matplotlib.patches import Rectangle
from matplotlib.pyplot import subplots, show
from wordcloud import WordCloud


#descompactando o arquivo zip         
#procon_zip= zipfile.ZipFile('C:\\Users\\lucia\Downloads\\consumer-business-complaints-in-brazil.zip')
#procon_zip.extractall('C:\\Users\\lucia\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.6\\procon_datasets')
#procon_zip.close()

#lendo os 5 arquivos csv do dataset do procon
procon_data1 = pd.read_csv('procon_datasets\\reclamacoes-fundamentadas-sindec-2012.csv')
#print(procon_data1.head())
procon_data2 = pd.read_csv('procon_datasets\\reclamacoes-fundamentadas-sindec-2013.csv')
#print(procon_data2.head())
procon_data3 = pd.read_csv('procon_datasets\\reclamacoes-fundamentadas-sindec-2014.csv')
#print(procon_data3.head())
procon_data4 = pd.read_csv('procon_datasets\\reclamacoes-fundamentadas-sindec-2015.csv')
#print(procon_data4.head())
procon_data5 = pd.read_csv('procon_datasets\\reclamacoes-fundamentadas-sindec-2016.csv')
#print(procon_data5.head())


#Integrando os 5 dataframes
dataframe_integrado = pd.concat([procon_data1, procon_data2, procon_data3, procon_data4, procon_data5])

#Transforma cada dataframe em uma lista(faz um cast do dataframe para a lista)
list1 = procon_data1.values.tolist()
list2 = procon_data2.values.tolist()
list3 = procon_data3.values.tolist()
list4 = procon_data4.values.tolist()
list5 = procon_data5.values.tolist()

#Integra os dataframes em uma lista única
lista_integrada = list1 + list2 + list3 + list4 + list5

#imprime texto explicativo

print('DIREITO DO CONSUMIDOR')
print('')
print('')

print('INTRODUÇÃO')
print('')
print('')

print('O Programa de Proteção e Defesa do Consumidor (PROCON), segundo [1], são fundações/autarquias que fazem parte do Sistema Nacional de Defesa do Consumidor, cujo objetivo é pensar e executar políticas públicas de proteção ao consumidor [2], através das Secretarias de Justiça e Cidadania de cada estado ou município.')
print('')
print('O PROCON é estabelecido primeiramente pelos governos estaduais e só depois está habilitado a ser criado pelos seus municípios.')
print('')
print('A função do PROCON é realizar a mediação e solução dos conflitos de interesses entre os consumidores e as empresas, defendendo os consumidores de quaisquer situações abusivas que sejam praticadas por indústrias, comércios e prestadores de serviço.')
print('')
print('O PROCON foi criado através da aprovação do Código de defesa do consumidor, momento  esse em que houve uma mudança do modo como as empresas se relacionam com os clientes [3].')
print('')
print('O PROCON: orienta os consumidores em suas reclamações, informa sobre seus direitos e fiscaliza as relações de consumo, tenta solucionar previamente os conflitos entre as partes envolvidas e quando não há acordo, ele encaminha o caso para o juizado especial cível com jurisdição sobre o local (regiões administrativas/"justiça de bairro") [4]') 
print('')
print('O DATASET')
print('')
print('O dataset fornecido para a pesquisa foi o Consumer Business Complaints in Brazil - Consumer complaints about issues with business in Brazil [5], hospedado no site Kaggle por Luiz Gerosa, líder técnico da Picpay.')
print('')
print('O dataset possui 1.206.072 registros, distribuídos entre os anos de 2012 a 2016 (ano calendário), que coincidem com os anos de arquivamento das reclamações.')
print('')
print('2012: possui 211.076 registros.')
print('2013: 268.096 registros.')
print('2014: 267.764 registros.')
print('2015: 255.650 registros.')
print('2016: 203.486 registros.')
print('')
print('A sua estrutura contém nas colunas os campos:')
print('')
print ('AnoCalendario\nDataArquivamento: data de arquivamento das reclamações\nDataAbertura: data de abertura das reclamações\nCodigoRegiao: índices atribuídos às regiões correspondentes aos agrupamentos das unidades da federação constantes no mapa político do Brasil\nRegião: regiões correspondentes aos agrupamentos das unidades da federação constantes no mapa político do Brasil\nUF: estados brasileiros\nstrRazaoSocial: razão social das empresas\nstrNomeFantasia: nome comercial ou de fachada das empresas\nTipo\nNumeroCNPJ\nRadicalCNPJ\nRazaoSocialRFB\nNomeFantasiaRFB\nCNAEPrincipal\nDescCNAEPrincipal\nAtendida\nCodigoAssunto\nDescriçãoAssunto\nCodigoProblema\nSexoConsumidor\nFaixaEtariaConsumidor\nCEPConsumidor.')
print('')

print('Optou-se por trabalhar com toda a população do dataset, pois havia um equacionamento interessante entre quantidade de dados versus poder de processamento versus qualidade da informação obtida.')
print('')
print('')

print('PERGUNTA DE PESQUISA')
print('')

print('De que forma podemos criar visualizações de informação com o objetivo de avaliar a eficácia do PROCON na proteção dos direitos dos consumidores?')
print('')

print('SUBPERGUNTAS')
print('')

print('A pergunta de pesquisa foi desdobrada nas questões a seguir:')
print('')

print ('Qual é a proporção do sexo dos reclamantes?\nQuem ganha mais processos (por sexo)?\nQuais são as faixas etárias que mais entram com reclamações no PROCON?\nQuais são as faixas etárias que ganham mais processos?\nquais são as faixas etárias e sexo que ganham mais processos?\nQuais são os tipos de assuntos mais comuns abordados nas reclamações?\nQuais são os tipos de problemas mais comuns abordados nas reclamações?\nComo clusterizar os tipos de problemas? Será possível, dadas as ferramentas que utilizamos?\nQuais são as regiões mais afetadas por problemas?\nEm quais regiões as pessoas efetivamente ganham mais processos?\nEm quais regiões as pessoas efetivamente perdem mais processos?\nDá pra saber de quais bairros pertencem as pessoas que ganham e perdem mais processos?\nSeria possível clusterizar essa informação, dadas as ferramentas que disponibilizamos?\nComo será a curva de crescimento das reclamações?\nComo será a curva de crescimento dos processos resolvidos com ganho de causa para o consumidor?\nComo será a curva de crescimento dos processos resolvidos com ganho de causa para as empresas?')
print('')


print('ANÁLISE')
print('')

print('Iniciou-se o trabalho pela pesquisa da proporção de reclamantes, por sexo e percebeu-se que não há diferença significativa entre os dois sexos no quesito reclamações, comportando-se igualitariamente os sexos feminino e masculino no questionamento dos seus direitos como consumidores(as).')
print('')


#Dados demográficos

#gênero

#Qual é o gênero dos participantes? 
lista_sexo = dict (dataframe_integrado.groupby('SexoConsumidor')['AnoCalendario'].count())

#agrupa as features (labels) e valores do dicionário em uma lista
labels = list (lista_sexo.keys())
#print(labels)
values = list (lista_sexo.values())
#print(values)

#Qual é a porcentagem de homens e mulheres reclamantes ao longo dos anos calendário de 2012 a 2016?
plt.pie(values, labels=labels, colors = ['#5C31A5', '#269085', '#020B10'], autopct='%1.1f%%')
centre_circle = plt.Circle((0,0),0.75,color='black', fc='white',linewidth=1.25)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title('Proporção de reclamantes, por sexo, de 2012 a 2016')
plt.axis('equal')
plt.show()
plt.close()
parada = input('aperte enter para continuar')

#Faixa etária
print('')

print('Já com relação à frequência de reclamações por faixa etária, a nossa população se comporta como se pode visualizar no gráfico a seguir, destacando-se os consumidores com idade entre 31 e 40 como sendo os que mais fazem reclamações e os que possuem mais de 70 anos como os que fazem menos reclamações.')
print('')
print('É importante atentar para o fato de que a faixa que compreende os consumidores que possuem “até 20 anos” naturalmente compreende um intervalo menor de consumidores, uma vez que só é possível fazer reclamações a partir de 18 anos (maioridade).')
print('')

#lista os códigos do problema

c = list (dataframe_integrado['FaixaEtariaConsumidor'])

#removendo dados sem relevância para a pesquisa
c = [x for x in c if x != 'Nao se aplica' and x != 'Nao Informada']


#plota um histograma com as faixas etárias cujas reclamações são mais frequentes
num_bins = 7

fig, ax = subplots(figsize = (15,7))
n, bins, patches = ax.hist(c, num_bins, rwidth=0.85)
ax.set_ylabel('Frequência', fontsize = 16)
ax.set_xlabel('Faixa Etária', fontsize = 16)
ax.set_title('Número de Reclamações por Faixa Etária', fontsize = 20)


#visualização da informação do histograma
i=0
cores= [ 'red', '#0077ff', 'green', 'blue', 'yellow', 'purple', 'orange']

while i<=6:
    patches[i].set_facecolor(cores[i])
    i=i+1


handles = [Rectangle ((0,0), 1, 1, color = c, ec = 'k') for c in cores]
labels = ['até 20 = '+ str(c.count('até 20 anos')), '21 a 30 = '+ str(c.count('entre 21 a 30 anos')), '31 a 40 = '+ str(c.count('entre 31 a 40 anos')), '41 a 50 = '+ str(c.count('entre 41 a 50 anos')), '51 a 60 = '+ str(c.count('entre 51 a 60 anos')), '61 a 70 = '+ str(c.count('entre 61 a 70 anos')) , 'mais de 70 = '+str(c.count('mais de 70 anos'))]
ax.legend(handles, labels)

# visualização da informação #retirando os ticks do eixo x
ax.tick_params(axis = 'x', which = 'both', bottom = 'off', top = 'off', labelbottom = 'off')
ax.grid(False)
ax.set_facecolor('white')
show()
plt.close()
parada = input('aperte enter para continuar')

print('')


#gerando gráfico de linhas entre reclamações atendidas e não atendidas de homens e mulheres agrupadas por ano

print('Em tempo: pensamos que seria importante saber não só qual era a proporção entre os reclamantes, segundo seus sexos, mas também que seria importante entender a evolução dos resultados dos atendimentos do PROCON, por sexo, ao longo dos anos.') 
print('')

plt.figure(figsize = (15,7))
lista_anos_s = dataframe_integrado.loc[dataframe_integrado['Atendida'] == 'S']
lista_anos_s_m = dict(lista_anos_s.loc[lista_anos_s['SexoConsumidor'] == 'M'].groupby('AnoCalendario')['AnoCalendario'].count())
lista_anos_s_f = dict(lista_anos_s.loc[lista_anos_s['SexoConsumidor'] == 'F'].groupby('AnoCalendario')['AnoCalendario'].count())

labels_m = list(lista_anos_s_m.keys())
values_m = list(lista_anos_s_m.values())
plt.plot(labels_m, values_m, 'g.-', label = 'Homens Atendidos', color = 'purple')

labels_f = list(lista_anos_s_f.keys())
values_f = list(lista_anos_s_f.values())
plt.plot(labels_f, values_f, 'g.-', label = 'Mulheres Atendidas', color = 'orange')

lista_anos_n = dataframe_integrado.loc[dataframe_integrado['Atendida'] == 'N']
lista_anos_n_m = dict(lista_anos_n.loc[lista_anos_n['SexoConsumidor'] == 'M'].groupby('AnoCalendario')['AnoCalendario'].count())
lista_anos_n_f = dict(lista_anos_n.loc[lista_anos_n['SexoConsumidor'] == 'F'].groupby('AnoCalendario')['AnoCalendario'].count())

labels_m = list(lista_anos_n_m.keys())
values_m = list(lista_anos_n_m.values())
plt.plot(labels_m, values_m, 'g.-', label = 'Homens Não Atendidos', color = '#0077ff')

labels_f = list(lista_anos_n_f.keys())
values_f = list(lista_anos_n_f.values())
plt.plot(labels_f, values_f, 'g.-', label = 'Mulheres Não Atendidas', color = 'lime')

plt.legend()
plt.xlim(2012, 2016)
plt.ylim(0, 100000)
plt.xticks(range(2011, 2018))
plt.title ('Resultado dos Atendimentos por Sexo - Evolução Histórica', fontsize = 20)
plt.ylabel('Número de atendimentos do PROCON', fontsize = 16)
plt.xlabel('Período Pesquisado', fontsize = 16)

plt.grid(True)

plt.show()
plt.close()
parada = input('aperte enter para continuar')

print('')

print('Constatamos assim que entre os anos de 2012 e 2016 houve uma variação de ganho no atendimento dos pleitos, favorável às mulheres, que se manteve na faixa quase constante de aproximadamente 10.000 pedidos atendidos.')
print('')
print('Já com relação aos resultados desfavoráveis, para o mesmo intervalo de tempo estudado, houve uma diferença de aproximadamente 4.000 causas com desfecho desfavorável para mulheres com relação às causas com desfecho desfavorável para aos homens. Dessa vez os homens levaram vantagem.')
print('')

#Gráfico de total de atendimentos por região - Evolução histórica

print('As regiões que se destacam no número de reclamações arquivadas são as regiões sudeste e nordeste, habitando a faixa que se estende de 80.000 a 100.000 arquivamentos e praticamente convergindo em número de arquivamentos no ano de 2014 (mais de 90.000 atendimentos). Interessante notar que no ano de 2016, a região sudeste deixa de apresentar vantagem no número de arquivamentos, sendo substituída pela região nordeste.')
print('')
print('Note que, para o ano de 2012, há uma lacuna de aproximadamente 65.000 entre a média aritmética dos arquivamentos das regiões norte e sul (aproximadamente 10.500 arquivamentos e a média dos arquivamentos das regiões sudeste e nordeste (75.000, aproximadamente), podendo indicar que estes realizam seu fluxo de trabalho de forma mais eficiente ou que nas regiões sudeste e nordeste os consumidores estão reclamando menos.')
print('')
print('A região centro-oeste habita a o centro do gráfico, apresentando uma quantidade de arquivamentos que oscila em torno da faixa dos 40.000 entre os anos de 2012 a 2015, surpreendendo negativamente ao revelar uma tendência de aproximação da faixa dos 30.000 no ano de 2016, aproximando-se das quantidades de atendimentos esboçadas pelas regiões sul e norte, as que menos atenderam consumidores no período estudado no ano calendário.')   
print('')
print('OBS: Quando falamos sobre menor número de atendimentos, entendemos que atender significa prestar o serviço para quem o procura. Sendo assim, casos em que o consumidor não procura o procon por quaisquer motivos, podem ocasionar uma tendência baixa no gráfico de total de atendimentos por região.')
print('')

plt.figure(figsize = (15,7))

lista_norte = dict(dataframe_integrado.loc [dataframe_integrado ['Regiao'] == 'Norte'].groupby('AnoCalendario')['AnoCalendario'].count())

lista_nordeste = dict(dataframe_integrado.loc [dataframe_integrado ['Regiao'] == 'Nordeste'].groupby('AnoCalendario')['AnoCalendario'].count())

lista_centrooeste = dict(dataframe_integrado.loc [dataframe_integrado ['Regiao'] == 'Centro-oeste'].groupby('AnoCalendario')['AnoCalendario'].count())

lista_sudeste = dict(dataframe_integrado.loc [dataframe_integrado ['Regiao'] == 'Sudeste'].groupby('AnoCalendario')['AnoCalendario'].count())

lista_sul = dict(dataframe_integrado.loc [dataframe_integrado ['Regiao'] == 'Sul'].groupby('AnoCalendario')['AnoCalendario'].count())

labels_norte = list(lista_norte.keys())
values_norte = list(lista_norte.values())
plt.plot(labels_norte, values_norte, 'bo:', label = 'Norte', color = 'purple')

labels_nordeste = list(lista_nordeste.keys())
values_nordeste = list(lista_nordeste.values())
plt.plot(labels_nordeste, values_nordeste, 'gv:', label = 'Nordeste', color = 'orange')

labels_centrooeste = list(lista_centrooeste.keys())
values_centrooeste = list(lista_centrooeste.values())
plt.plot(labels_centrooeste, values_centrooeste, 'g1:', label = 'Centro-oeste', color = 'magenta')

labels_sudeste = list(lista_sudeste.keys())
values_sudeste = list(lista_sudeste.values())
plt.plot(labels_sudeste, values_sudeste, 'gs:', label = 'Sudeste', color = 'blue')

labels_sul = list(lista_sul.keys())
values_sul = list(lista_sul.values())
plt.plot(labels_sul, values_sul, 'g*:', label = 'Sul', color = 'green')


plt.legend()
plt.xlim(2012, 2016)
plt.xticks(range(2011, 2018))
plt.title ('Total de Atendimentos por Região - Evolução Histórica', fontsize = 20)
plt.ylabel('Número de atendimentos do PROCON', fontsize = 16)
plt.xlabel('Período Pesquisado', fontsize = 16)
plt.grid(True)
plt.show()
plt.close()
parada = input('aperte enter para continuar')


#gerando uma wordcloud para a coluna DescricaoAssunto, que descreve o assunto da reclamação
print('')

print('Neste relatório geramos três nuvens de palavras com o objetivo de conhecer melhor a frequência dos termos que: 1- revelam os temas (produtos/serviços) constantes nas reclamações; 2- revelam os problemas que ocasionaram as reclamações (sobre os produtos/serviços); 3- revelam as pessoas jurídicas que geram mais reclamações ao PROCON.')
print('')
print('Na primeira nuvem de palavras, como se pode verificar, os termos mais frequentes estão relacionados ao ramo das telecomunicações.')
print('')

group_assuntos = dict (dataframe_integrado.groupby('DescricaoAssunto')['AnoCalendario'].count())

labels = list (group_assuntos.keys())
values = list (group_assuntos.values())

# lendo o texto todo
text = ''
i = 0
while i< len(labels):
    string = (labels[i] + ' ') * values[i]
    text += string
    i+=1

#removendo as stopwords
stopwords = set(['a', 'ante', 'após', 'até', 'com', 'contra', 'de', 'desde', 'em', 'ante', 'para', 'per', 'perante', 'por', 'sem', 'sob', 'sobre', 'traz','etc', 'primeiro', 'segundo', 'terceiro', 'quarto', 'quinto', 'sexto', 'sétimo', 'oitavo', 'nono', 'décimo', 'outro', 'ex', 'não', 'sim', 'na', 'no', 'da', 'do', 'ao','1º' ])

#cria a claoud
wordcloud = WordCloud(max_font_size=40, stopwords = stopwords, background_color = 'black', collocations = False).generate(text)
plt.figure(figsize = (15,7))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
parada = input('aperte enter para continuar')

#gerando uma wordcloud para a coluna DescricaoProblema, que descreve o problema da reclamação
print('')

print('Na segunda nuvem, como se pode notar, os termos mais frequentes indicam uma relação forte com o cumprimento de disposições contratuais para o período pesquisado.')
print('')

group_problemas = dict (dataframe_integrado.groupby('DescricaoProblema')['AnoCalendario'].count())

labels = list (group_problemas.keys())
values = list (group_problemas.values())

#lendo o texto todo
text = ''
i = 0
while i< len(labels):
    string = (labels[i] + ' ') * values[i]
    text += string
    i+=1

#cria a cloud
wordcloud = WordCloud(max_font_size=40, stopwords = stopwords, background_color = 'black', collocations = False).generate(text)
plt.figure(figsize = (15,7))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
parada = input('aperte enter para continuar')


#gerando uma word cloud como a coluna strNomeFantasia
print('')

print('Na terceira nuvem, são relacionadas as empresas alvo de maior número de reclamações ao longo do período observado. Observamos que há um grupo considerável de empresas relacionadas ao campo das telecomunicações, o que revela uma sinergia de informação com a primeira nuvem plotada. Veja só:')
print('')

group_nomes = dict (dataframe_integrado.groupby('strNomeFantasia')['AnoCalendario'].count())

labels = list (group_nomes.keys())
values = list (group_nomes.values())

#lendo o texto inteiro.
text = ''
i = 0
while i< len(labels):
    string = (labels[i] + ' ') * values[i]
    text += string
    i+=1

#cria a cloud
wordcloud = WordCloud(max_font_size=40, stopwords = stopwords, background_color = 'black', collocations = False).generate(text)
plt.figure(figsize = (15,7))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
parada = input('aperte enter para continuar')


#número de reclamações consolidadas para o período que compreende os anos calendário de 2012 a 2016
print('')

print('Este último gráfico mostra que o número de reclamações arquivadas no ano de 2012 ultrapassou a marca de 200.000, projetando-se para ultrapassar a marca dos 250.000 entre os anos de 2013 a 2015. Porém, em 2016 podemos observar uma retração no número de processos arquivados. Que pode se dever a diversos fatores, entre eles: aumento da inflação e consequente queda no poder de compra do consumidor; aumento da burocracia no fluxo que leva até o arquivamento das reclamações; diminuição das reclamações devido à inexperiência com questões jurídicas por parte do consumidor; elevação do padrão de atendimento e dos produtos oferecidos pelas empresas, etc.')
print('')

ano2012 = len(list1)
#print (len(list1))
ano2013 = len(list2)
#print (len(list2))
ano2014 = len(list3)
#print (ano2014)
ano2015 = len(list4)
#print (ano2015)
ano2016 = len(list5)
#print (ano2016)
 
#cria gráfico de barras horizontal
fig, ax = plt.subplots(figsize = (15,7))

#data
anos = [2012, 2013, 2014, 2015, 2016]
reclamacoes = [ano2012, ano2013, ano2014, ano2015, ano2016]  

#plota gráfico
ax.barh(anos,reclamacoes, color = '#C6CE51')
ax.set_yticks(anos)
ax.set_yticklabels(anos)
#ax.invert_yaxis() 
ax.set_xlabel('Reclamações')
ax.set_title('Reclamações no período de 2012 a 2016 (ano calendário)')
plt.grid(True, axis = 'x')
plt.show()
parada = input('aperte enter para continuar')

print('')
print('')

print('CONCLUSÕES')
print('')

print('Para trabalhos futuros pretende-se explorar mais profundamente a análise de informações em linguagem natural, utilizando, entre outras a biblioteca Natural Language Toolkit (NLTK) para Python. Considera-se que utilização de algoritmos de clusterização e predição de informações permitam resultados diferenciados no estudo deste dataset. A integração deste dataset com dados das redes sociais poderiam permitir um diagnóstico da satisfação da população (em geral, não só a população do dataset) com o trabalho realizado pelo PROCON, através, por exemplo da análise de sentimentos com relação aos serviços prestados no período compreendido no ano calendário em estudo.')
print('')

print('REFERÊNCIAS')
print('')

print('[1] https://goo.gl/xxE1PA\n[2] Lei 8078/90\n[3] https://goo.gl/LzeUX9\n[4] http://www.tjrj.jus.br/ca/institucional/juiz_especiais/juiz_especiais\n[5] https://www.kaggle.com/gerosa/procon/data') 

parada = input('aperte enter para sair')











