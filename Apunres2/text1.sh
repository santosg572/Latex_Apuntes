#!/bin/bash

pdflatex ${1}.tex 
bibtex ${1}

pdflatex ${1}.tex 
pdflatex ${1}.tex 

rm ${1}.aux ${1}.bbl  ${1}.blg  ${1}.log  

okular ${1}.pdf


