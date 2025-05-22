import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,30,0))
r=w0.sketch().segment((-100,3),(-18,3)).segment((-18,63)).segment((-34,63)).segment((-34,75)).segment((-65,75)).segment((-65,63)).segment((-100,63)).close().assemble().push([(-75,32)]).circle(10,mode='s').finalize().extrude(-61).union(w0.workplane(offset=-48/2).moveTo(77,-52).cylinder(48,23))