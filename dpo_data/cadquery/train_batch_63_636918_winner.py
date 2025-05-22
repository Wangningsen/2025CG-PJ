import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,78,0))
r=w0.sketch().push([(-37,-9)]).circle(63).circle(29,mode='s').reset().face(w0.sketch().segment((24,58),(57,-38)).segment((97,-24)).segment((64,72)).close().assemble()).finalize().extrude(-155).union(w0.workplane(offset=-62/2).moveTo(60,19).cylinder(62,40))