# Python-a-Cython
En el repositorio descansan dos archivos, uno con hecho en phyton3 (cy_planeta) y la conversion del mismo codigo a cython (cy_planeta)

en el repositorio encontramos 3 codigos más, un Makefile, un Setup y un codigo en phyton3 llamado Perfomance.

Inicialmente se usa el MakeFile para hacer una compilacion limpia del codigo que desea ejecutar usando el comoando MakeAll

En el setup se cytoniza el archivo y se crea el build, con ello, se ejecutara el archivo "Perfomance.py" con el cual se tomarán los segundos
de procesamiento entre el codigo de python, y el codigo de cython, para finalmente crear el .csv con los resultados
