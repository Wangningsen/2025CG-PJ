import cadquery as cq
w0=cq.Workplane('YZ',origin=(37,0,0))
w1=cq.Workplane('ZX',origin=(0,1,0))
r=w0.workplane(offset=-137/2).cylinder(137,69).union(w1.sketch().arc((27,4),(54,52),(27,100)).segment((27,54)).segment((45,54)).segment((45,31)).segment((27,31)).close().assemble().finalize().extrude(-25))