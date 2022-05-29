all:
	rm -f mul_c
	rm -f mul_py
	gcc -fPIC -shared -o libutils.so utils.c
	python3 task10.py
	diff mul_c mul_py
