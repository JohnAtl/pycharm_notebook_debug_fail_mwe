# pycharm_notebook_debug_fail_mwe
- Load the notebook mwe.ipynb
- Run the first cell
- Click debug on the second cell
- Press F11

This is the error:
```aiignore
Traceback (most recent call last):
  File "/var/home/john/Apps/pycharm/pycharm-2025.2.0.1/plugins/python-ce/helpers/pydev/_pydevd_bundle/pydevd_comm.py", line 736, in make_thread_stack_str
    append('file="%s" line="%s">' % (make_valid_xml_value(my_file), lineno))
                                     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/var/home/john/Apps/pycharm/pycharm-2025.2.0.1/plugins/python-ce/helpers/pydev/_pydevd_bundle/pydevd_xml.py", line 36, in make_valid_xml_value
    return s.replace("&", "&amp;").replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
           ^^^^^^^^^
AttributeError: 'tuple' object has no attribute 'replace'
```
