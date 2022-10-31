import time
import codigo_phyton
import codigo_chyton

codigochyton = codigo_chyton.Planet()
codigophyton = codigo_phyton.Planet()
init_time = time.time()
codigo_phyton.step_time(codigophyton, 50,4)
fin_time = time.time()
total_time_python = fin_time - init_time
print("tiempo total python: ", total_time_python)


init_time = time.time()
codigo_chyton.c_step_time(planeta_cy, 50,4)
fin_time = time.time()
total_time_cython = fin_time - init_time
print("tiempo total cython: ", total_time_cython)