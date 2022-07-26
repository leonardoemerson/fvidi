# FVIDI

Este repositório contém uma ferramenta de visualização interativa de dados interligados (FVIDI) desenvolvida por Leonardo Emerson.<br>
A pasta *consultas* contém as Queries usadas para experimentação da ferramenta.<br>
A pasta *visualizations* contém as visualizações geradas pela ferramenta na etapa de experimentação.<br>
Para executar a ferramenta localmente, acesse a pasta ou diretório onde se localiza o arquivo "FVIDI.py" e execute o comando: streamlit run "FVIDI.py".<br>
OBS.: É necessário ter as bibliotecas e dependências do projeto previamente instaladas para a correta execução da ferramenta.

## Consultas usadas para experimentação da ferramenta

- Consulta 1 - Origem das vacinas de Covid 19

```sparql
SELECT DISTINCT ?vaccineLabel ?originCountry  {
  ?vaccine wdt:P1924 wd:Q84263196 .
  ?vaccine wdt:P178 ?developer.
  ?vaccine rdfs:label ?vaccineLabel .
  ?developer wdt:P17 ?origin . 
  ?origin rdfs:label ?originCountry .
  FILTER (LANG(?vaccineLabel) = 'en').
  FILTER (LANG(?originCountry) = 'en').
}LIMIT 25
```

- Visualização 1 - Sunburst
![alt text](https://github.com/leonardoemerson/fvidi/blob/main/visualizations/Visualização%201.png?raw=true)

- Consulta 2 - Casos, recuperações e óbitos de Covid 19

```sparql
SELECT ?tempo ?Recuperacoes ?Casos ?Obitos WHERE {
  {
    SELECT ?tempo ?Recuperacoes WHERE {
      wd:Q84263196 p:P8010 ?countRes .
      FILTER NOT EXISTS { ?countRes pq:P276 ?loc }
      ?countRes ps:P8010 ?Recuperacoes ;
                   pq:P585 ?tempo .
    }
  } 
{
    SELECT ?tempo ?Casos WHERE {
      wd:Q84263196 p:P1603 ?countRes .
      FILTER NOT EXISTS { ?countRes pq:P276 ?loc }
       ?countRes ps:P1603 ?Casos ;
                   pq:P585 ?tempo .
    }
  } 
  {
    SELECT ?tempo ?Obitos WHERE {
      wd:Q84263196 p:P1120 ?countRes .
      FILTER NOT EXISTS { ?countRes pq:P276 ?loc }
       ?countRes ps:P1120 ?Obitos ;
                   pq:P585 ?tempo .
    }
  }
}
```

- Visualização 2.1 - Heatmap
![alt text](https://github.com/leonardoemerson/fvidi/blob/main/visualizations/Visualização%202.1.png?raw=true)

- Visualização 2.2 - StackedAreChart
![alt text](https://github.com/leonardoemerson/fvidi/blob/main/visualizations/Visualização%202.2.png?raw=true)

- Consulta 3 - Número de Casos de Covid 19 por data

```sparql
SELECT ?data ?numeroDeCasos WHERE {
  wd:Q81068910 p:P1603 ?numeroDeCasosStat .
  ?numeroDeCasosStat ps:P1603 ?numeroDeCasos ;
                     pq:P585 ?data .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en,en". }
} ORDER BY ASC(?data)
```
- Visualização 3 - LineChart
![alt text](https://github.com/leonardoemerson/fvidi/blob/main/visualizations/Visualização%203.png?raw=true)

- Consulta 4 - Profissão das pessoas que faleceram de Covid 19
```sparql
SELECT ?occupation ?occupationLabel (COUNT(*) as ?count) WHERE {
  ?person wdt:P509 wd:Q84263196 ; wdt:P31 wd:Q5 .
  ?person wdt:P106 ?occupation .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en" } .
} 
GROUP BY ?occupation ?occupationLabel
ORDER BY DESC(?count)
LIMIT 30
```
- Visualização 4 - BubbleChart
![alt text](https://github.com/leonardoemerson/fvidi/blob/main/visualizations/Visualização%204.png?raw=true)

- Consulta 5 - Distribuição de idade de famosos que faleceram de Covid 19

```sparql
SELECT ?age (COUNT(?person) AS ?count) WHERE {
{SELECT ?person (SAMPLE(?age) AS ?age)  WHERE {
    ?person wdt:P509 wd:Q84263196 ; wdt:P31 wd:Q5 
    OPTIONAL { ?person wdt:P570 ?d }
    ?person wdt:P569 ?dob ; wdt:P570 ?dod . BIND(YEAR(?dod)-YEAR(?dob) as ?age) 
     SERVICE wikibase:label {
    bd:serviceParam wikibase:language "en" .
   }
 } GROUP BY ?person
}
} GROUP BY ?age

```

- Visualização 5 - Histogram
![alt text](https://github.com/leonardoemerson/fvidi/blob/main/visualizations/Visualização%205.png?raw=true)
