def personal_openProject():
    import console
    from qgis.utils import iface
    from qgis.PyQt.QtWidgets import QDockWidget

    pythonConsole = iface.mainWindow().findChild(QDockWidget, 'PythonConsole')
    if not pythonConsole or not pythonConsole.isVisible():
        iface.actionShowPythonDialog().trigger()

def personal_saveProject():
    pass

def personal_closeProject():
    pass
