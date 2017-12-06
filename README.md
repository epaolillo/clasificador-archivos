# Analizador de Textos

[![Coverage Status](https://coveralls.io/repos/github/datosgobar/textar/badge.svg?branch=master)](https://coveralls.io/github/datosgobar/textar?branch=master)
[![Build Status](https://travis-ci.org/datosgobar/textar.svg?branch=master)](https://travis-ci.org/datosgobar/textar)
[![PyPI](https://badge.fury.io/py/textar.svg)](http://badge.fury.io/py/textar)
[![Stories in Ready](https://badge.waffle.io/datosgobar/textar.png?label=ready&title=Ready)](https://waffle.io/datosgobar/textar)
[![Documentation Status](http://readthedocs.org/projects/textar/badge/?version=latest)](http://textar.readthedocs.org/en/latest/?badge=latest)

Paquete en python para análisis, clasificación y recuperación de textos, utilizado por el equipo de Datos Argentina.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Instalación](#instalaci%C3%B3n)
  - [Dependencias](#dependencias)
  - [Desde pypi](#desde-pypi)
  - [Para desarrollo](#para-desarrollo)
- [Uso](#uso)
  - [Búsqueda de textos similares](#b%C3%BAsqueda-de-textos-similares)
  - [Clasificación de textos](#clasificaci%C3%B3n-de-textos)
- [Tests](#tests)
- [Créditos](#cr%C3%A9ditos)
- [Contacto](#contacto)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

* Licencia: MIT license

## Instalación

### Dependencias

`textar` usa `pandas`, `numpy`, `scikit-learn` y `scipy`. Para que funcionen, se requiere instalar algunas dependencias no pythonicas:

* En Ubuntu: `sudo apt-get install libblas-dev liblapack-dev libatlas-base-dev gfortran`

### Desde pypi

`pip install textar`

### Para desarrollo

```
git clone https://www.github.com/datosgobar/textar.git
cd path/to/textar
pip install -e .
```

Cualquier cambio en el código está disponible en el entorno virtual donde fue instalado de esta manera.

## Uso

### Búsqueda de textos similares



### Clasificación de textos

```python
# requiere textar
# requiere numpy, glob, textract, warning

from textar import TextClassifier
from numpy import array
import glob
import textract
import warnings

textos = []
puntajes = []
ejem = []
etiquetas = []

# Si o si deben ser 3 datasets
dispos = glob.glob("/home/ezequiel/Descargas/entrena/dispo/*.pdf");
informes = glob.glob("/home/ezequiel/Descargas/entrena/informe/*.pdf");
otros = glob.glob("/home/ezequiel/Descargas/entrena/otro/*.pdf");

testers = glob.glob("/home/ezequiel/Descargas/ejem/*.pdf");


for informe in informes:
      cadena = textract.process(informe, method='pdfminer')
      textos.append(cadena)
      etiquetas.append("Informe")
      
for otro in otros:
      cadena = textract.process(otro, method='pdfminer')
      textos.append(cadena)
      etiquetas.append("Otro")
      
for dispo in dispos:
      cadena = textract.process(dispo, method='pdfminer')
      textos.append(cadena)   
      etiquetas.append("Dispo")   
      
for archivo in testers:
      cadena = textract.process(archivo, method='pdfminer')
      ejem.append(cadena)      
      
print("Archivos:")
print(dispos);
print(informes);

print(testers);
print("--------")
print(etiquetas)

largoTotal = len(informes)+len(dispos)+len(otros)

tc = TextClassifier( textos, ids=map(str, range(largoTotal)) )


# entrena un clasificador
tc.make_classifier(
    name="recetas_classifier",
    ids=map(str, range(largoTotal)),
    labels=etiquetas
)

labels_considerados, puntajes = tc.classify(
    classifier_name="recetas_classifier", 
    examples = ejem
)

print labels_considerados
print puntajes


for index , x in enumerate(testers):
    print "-----------"
    print x
    print puntajes[index]
    es = sorted(zip(puntajes[index], labels_considerados), reverse=True)
    print es[0][1]
    print "-----------"


```

## Tests

Los tests sólo se pueden correr habiendo clonado el repo. Luego instalar las dependencias de desarrollo:

`pip install -r requirements_dev.txt`

y correr los tests:

`nosetests`

## Créditos

* [Victor Lavrenko](http://homepages.inf.ed.ac.uk/vlavrenk/) nos ayudó a entender el problema con sus explicaciones en youtube: https://www.youtube.com/user/victorlavrenko

## Contacto

Te invitamos a [crearnos un issue](https://github.com/datosgobar/textar/issues/new?title=Encontré un bug en textar) en caso de que encuentres algún bug o tengas feedback de alguna parte de `textar`.

Para todo lo demás, podés mandarnos tu comentario o consulta a [datos@modernizacion.gob.ar](mailto:datos@modernizacion.gob.ar).
# clasificador-archivos
