#!/bin/bash

file=$1

pdflatex ${1}.tex

rm *.aux
rm *.log
rm *.nav
rm *.out
rm *.snm
rm *.toc

open ${1}.pdf
