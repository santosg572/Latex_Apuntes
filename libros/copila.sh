#!/bin/bash

rm $1.pdf
rm $1.aux		
rm $1.log

pdflatex $1.tex

open $1.pdf
