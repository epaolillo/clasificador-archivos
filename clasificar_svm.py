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


