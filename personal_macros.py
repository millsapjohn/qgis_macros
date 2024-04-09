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
        proj_conn = QgsExpressionContextUtils.projectScope(project).variable('project_gpkg_connections').split(";")
        proj_uri = proj_conn[1::2]
        proj_conn = proj_conn[0::2]
        md = QgsProviderRegistry.instance().providerMetadata('ogr')
        if md.connections():
            for item in md.connections():
                if item not in proj_conn:
                    md.deleteConnection(item)
        for i in range(len(proj_conn) - 1):
            if proj_conn[i] not in md.connections():
                conn = md.createConnection(proj_uri[i])
                md.saveConnection(conn, proj_conn[i]) 
        iface.reloadConnections()

def personal_saveProject():
    pass

def personal_closeProject():
    pass
