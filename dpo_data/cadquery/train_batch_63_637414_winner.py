import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().arc((-19,86),(-63,-58),(76,-43)).segment((53,-43)).segment((53,-15)).segment((87,-15)).close().assemble().finalize().extrude(110).union(w0.workplane(offset=200/2).moveTo(0,1).cylinder(200,45))