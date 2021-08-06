#!/usr/bin/python3

import re
string="Podemos sufrir un problema de frases muy largas cuando encontramos muchas frases en el texto de más de tres o cuatro líneas (en un folio o A4, letra tamaño 12). En muchas ocasiones, en realidad, cada una de esas frases son varias frases distintas, que deberían estar separadas por puntos y están separadas por comas.Frases tan largas no ayudan a la naturalidad: la naturalidad es eso que hace que, al leer un relato, nos parezca estar oyendo a esa persona contando su historia y, por tanto, ésta nos resulte más creíble. Frases tan largas, sin embargo, suelen sonar teatrales, poco convincentes, además de ser mucho más complicadas de redactar… y llegar a crear errores gramaticales.Incluso cuando están impecablemente redactadas, las frases largas siempre resultan un poco confusas porque perdemos el hilo del comienzo y tenemos que releerlas. Sería muy sencillo separar estas frases en dos o tres, de forma que, sin variar un ápice la historia (ni lo que se dice, ni cómo se dice) quede más natural y más agradable de leer.Por supuesto, puede haber autores que buscan las frases largas como recurso estilístico (éstas imprimen un ritmo más lento a la narración, por ejemplo); pero si ese no es nuestro caso, debemos empezar por las frases más Breves."
countDict={}

def normalizarWord(word):
  #print (word)
  word = word.lower()
  #word = re.sub("\,|\),|\(","",string)
  #word = re.sub('[^a-zA-Z0-9 \n\.]', '', word)
  return word


for word in string.split(" "):
  wordNormlized=normalizarWord(word)
  print (wordNormlized)
  if wordNormlized in countDict:
    countDict[wordNormlized]+=1
  else:
    countDict[wordNormlized]=1
  
print (countDict)
    
