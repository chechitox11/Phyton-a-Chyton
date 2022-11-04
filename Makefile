all:
		python3 setup.py build ext --inplace
	
clean:
		rm -rf build *.so *.c *.pyc


