#include <stdio.h>
#include <stdlib.h>
#include <wchar.h>
#include <locale.h>
#include <Python.h>
#include <unicodeobject.h>

/**
 * print_python_sting - prints info about python strings
 * @p: address of pyobject struct
 */
void print_python_string(PyObject *p)
{
	wchar_t *w_str;
	
	wprintf(L"[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str"))
	{
		wprintf(L" [ERROR] Invalid String Object\n");
		return;
	}
	if (PyUnicode_IS_COMPACT_ASCII(p))
		wprintf(L" type: comapct ascii\n");
	else
		wprintf(L" type: compact unicode object\n");
	wprintf(L" length: %lu\n", PyUnicode_GET_LENGTH(p));
	
	w_str = PyUnicode_AsWideCharString(p, NULL);
    if (w_str == NULL)
    {
        wprintf(L"  [ERROR] Cannot convert to wide char string\n");
        return;
    }

    wprintf(L"  value: %ls\n", w_str);
    PyMem_Free(w_str);
}
