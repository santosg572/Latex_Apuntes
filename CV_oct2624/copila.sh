#!/bin/bash

pdflatex ${1}.tex

open ${1}.pdf
