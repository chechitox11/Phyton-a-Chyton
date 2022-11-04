import time
import py_planeta
import cy_planeta

init_time=time.time()
plan=py_planeta.Planet()
planeta_py.x = 100*10**3
planeta_py.y = 300*10**3
planeta_py.z = 700*10**3
planeta_py.vx = 2.000*10**3
planeta_py.vy = 29.87*10**3
planeta_py.vz = 0.034*10**3
planeta_py.m = 5.9741*10*24


planeta_cy.x = 100*10**3
planeta_cy.y = 300*10**3
planeta_cy.z = 700*10**3
planeta_cy.vx = 2.000*10**3
planeta_cy.vy = 29.87*10**3
planeta_cy.vz = 0.034*10**3
planeta_cy.m = 5.9741*10*24

time_spam = 400
n_steps=2000000

formato_datos = "{:,5f},{:,5f}\n" 
for i in range(2):
	iniciopy = time.time()
	py_planeta.step_time(planeta_py, time_span, n_steps)
	finalpy=time.time() - iniciopy
	
	iniciocy = time.time()
	cy_planeta.step_time(planeta_cy, time_span, n_steps)
	finalcy=time.time() - iniciocy
	
	
	with open("planeta.csv","a") as archivo:
		archivo.write(formato_datos.format((finalpy-finalcy))
	
	
	
