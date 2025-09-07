d1 = '''
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>
'''
d2 = '''
</body>
</html> 
'''

datos=["ejemplo01.pdf", "ejemplo02.pdf","ejemplo03.pdf","ejercicios_ago1325.pdf","p1.pdf","series_taylor.pdf","tarea01.pdf" ]

fil = open('libros.html','w')
fil.write(d1)

for ss in datos:
   ssp = '<p> '+ ss + ' </p>\n'
   ssa = '<iframe src="' + ss + '" width="100%" height="600px"></iframe>\n'
   fil.write(ssp)
   fil.write(ssa)

'''
<p>This is a paragraph.</p>


<iframe src="ejemplo02.pdf" width="100%" height="600px"></iframe>
<iframe src="ejemplo03.pdf" width="100%" height="600px"></iframe>
<iframe src="ejercicios_ago1325.pdf" width="100%" height="600px"></iframe>
<iframe src="series_taylor.pdf" width="100%" height="600px"></iframe>
<iframe src="tarea01.pdf" width="100%" height="600px"></iframe>
</body>
</html> 
'''

fil.write(d2)
fil.close()


