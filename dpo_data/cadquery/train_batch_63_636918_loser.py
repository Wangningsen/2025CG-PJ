import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,77,0))
r=w0.sketch().push([(-37,-9)]).circle(63).circle(29,mode='s').reset().face(w0.sketch().segment((23,58),(56,-34)).segment((97,-23)).segment((63,72)).close().assemble()).finalize().extrude(-154).union(w0.workplane(offset=-52/2).moveTo(62,11).cylinder(52,38))