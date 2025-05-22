import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().arc((-23,85),(-68,-52),(76,-43)).segment((53,-43)).segment((53,-15)).segment((87,-15)).segment((-19,86)).arc((-21,84),(-23,85)).assemble().finalize().extrude(110).union(w0.workplane(offset=200/2).moveTo(1,1).cylinder(200,45))