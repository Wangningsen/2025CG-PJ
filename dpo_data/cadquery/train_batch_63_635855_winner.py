import cadquery as cq
w0=cq.Workplane('YZ',origin=(4,0,0))
r=w0.sketch().segment((13,87),(59,48)).segment((73,65)).arc((37,67),(24,100)).close().assemble().finalize().extrude(-55).union(w0.workplane(offset=41/2).moveTo(-19,-46).cylinder(41,54)).union(w0.workplane(offset=46/2).moveTo(-19,-25).cylinder(46,24))