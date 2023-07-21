

t1 = ''' 
\\documentclass{beamer}
\\usepackage[spanish]{babel}
\\usepackage[latin1]{inputenc}

\\begin{document}

\\begin{frame}
    \\frametitle{Marsupiales} '''

t2= '''
    \\end{frame}

\\end{document}
'''

file = open('salida.tex', 'w')

file.write(t1)

tt = '''

este es un text,

$$
ax^2 + \\frac{3}{4} \pi
$$

aqui termina
'''

file.write(tt)
file.write(t2)

file.close()
