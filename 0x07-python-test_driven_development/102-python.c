#include <Python.h>
#include <wchar.h>

/**
 * print_python_string - prints info about Python strings.
 * @p: address of the PyObject struct (Python object).
 *
 * This function prints details about a Python string, including its type,
 * length, and value. If the object is not a valid Python string, an error
 * message is printed.
 */
void print_python_string(PyObject *p)
{
    wchar_t *w_str;

    printf("[.] string object info\n");

    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    if (PyUnicode_IS_COMPACT_ASCII(p))
        printf("  type: compact ascii\n");
    else
        printf("  type: compact unicode object\n");

    printf("  length: %ld\n", PyUnicode_GetLength(p));

    w_str = PyUnicode_AsWideCharString(p, NULL);
    if (w_str == NULL)
    {
        printf("  [ERROR] Cannot convert to wide char string\n");
        return;
    }

    wprintf(L"  value: %ls\n", w_str);
    PyMem_Free(w_str);  // Free the memory allocated by PyUnicode_AsWideCharString
}

