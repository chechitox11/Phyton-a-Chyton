all:
		python3 setup.py build ext --inplace
	
clean:
		tm -rf build *.so *.c *.pyc


