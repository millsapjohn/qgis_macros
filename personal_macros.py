def personal_openProject():
    import console
    from qgis.core import QgsExpressionContextUtils, QgsProviderRegistry, QgsProject
    from qgis.utils import iface
    from qgis.PyQt.QtWidgets import QDockWidget

    pythonConsole = iface.mainWindow().findChild(QDockWidget, 'PythonConsole')
    if not pythonConsole or not pythonConsole.isVisible():
        iface.actionShowPythonDialog().trigger()

    project = QgsProject.instance()
    if QgsExpressionContextUtils.projectScope(project).variable('project_gpkg_connections'):
        proj_conn = QgsExpressionContextUtils.projectScope(project).variable('project_gpkg_connections')
        md = QgsProviderRegistry.instance().providerMetadata('ogr')
        if md.connections() != {}:
            for key in md.connections().keys():
                if key not in proj_conn.keys():
                    md.deleteConnection(key)
        for key in proj_conn.keys():
            if key not in md.connections().keys():
                conn = md.createConnection(proj_conn[key])
                md.saveConnection(conn, key) 
        iface.reloadConnections()

def personal_saveProject():
    pass

def personal_closeProject():
    pass
