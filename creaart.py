#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
 
#print("Número de parámetros: " + str(len(sys.argv)))

nombreIn = sys.argv[1]

fi = open(nombreIn+'.txt', 'r')

tt = fi.read()
fi.close()

print(tt)

t1 = '''

\\documentclass[a4paper,14pt]{book}


\\usepackage[utf8]{inputenc}
\\usepackage[spanish,es-tabla]{babel}
\\usepackage[T1]{fontenc}
\\usepackage{hyperref}
\\hypersetup{
    colorlinks,
    citecolor=green,
    filecolor=blue,
    linkcolor=red,
    urlcolor=black
}

\\usepackage{listings}

\\usepackage{geometry}

\\geometry{
 tmargin=2.5cm,
 bmargin=2.5cm,
 lmargin=2.5cm,
 rmargin=2.5cm
}

% Comandos

\\renewcommand{\lstlistingname}{Código}
\\renewcommand{\lstlistlistingname}{Índice de fragmentos de código fuente}

% Opciones

\\title{Python 2.*}
\\author{Ondiz Zarraga}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\\begin{document}
\\maketitle


\\tableofcontents

'''

t2 = '''
\\begin{itemize}
    \\item Interpretado
    \\item Indentación obligatoria
    \\item Distingue mayúsculas - minúsculas
    \\item No hay declaración de variables (\textit{dynamic typing})
    \\item Orientado a objetos  
    \\item Garbage colector: quita los objetos a los que no haga referencia nada
\\end{itemize}
'''

t3 = '''
\end{document}
'''

f = open(nombreIn + '.tex', 'w')

f.write(t1)
f.write(tt)
f.write(t3)
f.close()



