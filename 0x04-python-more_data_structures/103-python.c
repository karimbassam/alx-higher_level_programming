#include <stdio.h>
#include <Python.h>

void print_python_list(PyObject *p)
{
    if (!PyList_Check(p))
    {
        fprintf(stderr, "Invalid List Object\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t i;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        PyObject *item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

void print_python_bytes(PyObject *p)
{
    if (!PyBytes_Check(p))
    {
        fprintf(stderr, "Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    Py_ssize_t i;
    char *string;

    printf("[.] bytes object info\n");
    printf("size: %ld\n", size);

    if (size > 10)
    {
        size = 10;
    }

    printf("trying string: %s\n", PyUnicode_AsUTF8(PyObject_Repr(p)));

    PyBytes_AsStringAndSize(p, &string, &size);

    printf("first %ld bytes: ", size);
    for (i = 0; i < size; i++)
    {
        printf("%02hhx", string[i]);
        if (i < size - 1)
            printf(" ");
    }
    printf("\n");
}
