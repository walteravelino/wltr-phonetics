# Wltr Phonetics

<a href="https://pypi.org/project/wltr-phonetics/">
  <img alt="PyPI" src="https://img.shields.io/pypi/v/wltr-phonetics">
</a>

[![Build Status](https://travis-ci.com/walteravelino/Projetos.svg?branch=master)](https://travis-ci.com/walteravelino/Projetos)
<img src = "https://img.shields.io/github/languages/top/walteravelino/jca-cleansing-validate">
<a href="https://github.com/walteravelino/Projetos/blob/master/LICENSE"><img src = "https://img.shields.io/github/license/walteravelino/Projetos"></a>

WltrPhonetics é uma biblioteca Python para algoritmos fonéticos. 
Os seguintes algoritmos estão disponíveis:

 * Soundex
 * Metaphone
 * Refined Soundex
 * Fuzzy Soundex
 * Lein
 * Matching Rating Approach
 
Além disso, as seguintes métricas de distância:

 * Hamming
 * Levenshtein

## Autor

👤 **Walter Avelino**

- StackOverFlow [@walteravelino](https://stackoverflow.com/users/13001807/walter-avelino)
- Github: [@walteravelino](https://github.com/walteravelino)
- Linkedin: [@walteravelino](https://linkedin.com/in/walter-avelino-434197105)
- DEV: [@walteravelino](https://dev.to/walteravelino)


## 📝 Licença

Copyright © 2020 [Walter Avelino](https://github.com/walteravelino). <br />
Os projetos estão sob a licença [MIT](https://github.com/walteravelino/Projetos/blob/master/LICENSE).


## Instalação


O módulo está disponível no PyPI, basta instalar pelo pip `pip install wltr-phonetics`.


## Utilização

```python
>>> from wltrphonetics import Soundex
>>> soundex = Soundex()
>>> soundex.phonetics('Walter')
'R163'
>>> soundex.phonetics('Waltie')
'R163'
>>> soundex.sounds_like('Walter', 'Waltie')
True
```

A mesma API se aplica a todos os algoritmos, por exemplo:

```python
>>> from wltrphonetics import Metaphone
>>> metaphone = Metaphone()
>>> metaphone.phonetics('discriminação')
'TSKRMNXN'
```

Você também pode usar o método `distance(word1, word2, metric='levenshtein')` para encontrar a distância entre 2 representações fonéticas.

```python
>>> from wltrphonetics import RefinedSoundex
>>> rs = RefinedSoundex()
>>> rs.distance('Walter', 'Waltie')
0
>>> rs.distance('assign', 'assist', metric='hamming')
2
```

## Créditos

O módulo foi amplamente baseado na implementação de algoritmos fonéticos encontrados em [Talisman.js](https://github.com/Yomguithereal/talisman) "Node NLP library".