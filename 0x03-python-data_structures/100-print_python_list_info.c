#include <stdio.h>
#include <Python.h>

void print_python_list_info(PyObject *p)
{
	Py_ssize_t lent = PyList_Size(p), i;
	Py_ssize_t temp = ((PyListObject *)p)->allocated;
	PyTypeObject *type;

	if (PyList_CheckExact(p))
	{
		printf("[*] Size of the Python List = %lu\n", lent);
		printf("[*] Allocated = %lu\n", temp);
		for (i = 0; i < lent; i++)
		{
			type = Py_TYPE(PyList_GetItem(p, i));
			printf("Element %lu: %s\n", i, type->tp_name);
		}
	}
}
