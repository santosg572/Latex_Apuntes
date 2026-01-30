#!/bin/bash

rm $1.pdf
pdflatex $1".tex"
open $1.pdf


