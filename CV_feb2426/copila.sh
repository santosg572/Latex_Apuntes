#!/bin/bash

pdflatex ${1}.tex

rm *.aux
rm *.log

open ${1}.pdf
