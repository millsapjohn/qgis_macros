# Macro Setup
In order to more easily manage macros with git, I've set them up as follows.<br>

In QGIS, edit your global variables to include the path to this repo's code. For
example, "win_macro_path", "mac_macro_path", etc. Then, in Project -> Properties -> Macros,
set the code as follows:

  import os
  from qgis.core import QgsExpressionContextUtils
  import sys

  curr_sys = QgsExpressionContextUtils.globalScope().variable('qgis_os_name')
  if curr_sys == 'windows':
    macro_path = QgsExpressionContextUtils.globalScope().variable('win_macro_path')
  else:
    macro_path = QgsExpressionContextUtils.globalScope().variable('linux_macro_path')
  sys.path.append(macro_path)

  from personal_macros import personal_openProject, personal_saveProject, personal_closeProject

  def openProject():
    personal_openProject()

  def saveProject():
    personal_saveProject()

  def closeProject():
    personal_closeProject()

Setting paths per OS is optional, but helps keep your code modular and flexible.

# open Project
Currently, the personal_openProject macro does two things:

1. activate the Python console
2. manage GeoPackage connections in concert with my [Project Setup Plugin](https://github.com/millsapjohn/qgis_project_setup).

# save Project
Currently does nothing

# close Project
Currently does nothing
