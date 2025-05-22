import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,33,0))
r=w0.sketch().arc((11,28),(-70,-52),(22,16)).arc((15,22),(11,28)).assemble().push([(29,46)]).circle(27).finalize().extrude(-133).union(w0.workplane(offset=-100/2).moveTo(20,0).cylinder(100,63)).union(w0.workplane(offset=67/2).moveTo(17,0).cylinder(67,38))