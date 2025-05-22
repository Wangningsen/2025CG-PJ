import cadquery as cq
w0=cq.Workplane('YZ',origin=(13,0,0))
r=w0.sketch().arc((24,39),(26,34),(27,29)).segment((74,29)).segment((74,100)).segment((24,100)).close().assemble().finalize().extrude(-43).union(w0.workplane(offset=16/2).moveTo(-43,-69).cylinder(16,31))