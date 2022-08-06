# FVIDI

Este repositório contém uma ferramenta de visualização interativa de dados interligados (FVIDI) desenvolvida por Leonardo Emerson.

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

- Consulta 3 - Número de Casos de Covid 19 por data

```sparql
SELECT ?data ?numeroDeCasos WHERE {
  wd:Q81068910 p:P1603 ?numeroDeCasosStat .
  ?numeroDeCasosStat ps:P1603 ?numeroDeCasos ;
                     pq:P585 ?data .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "en,en". }
} ORDER BY ASC(?data)
```

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
