import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,77,0))
r=w0.sketch().push([(-37,-9)]).circle(63).circle(29,mode='s').reset().face(w0.sketch().segment((23,58),(57,-38)).segment((97,-24)).segment((63,72)).close().assemble()).finalize().extrude(-155).union(w0.sketch().push([(60,17)]).circle(40).push([(57.5,25)]).rect(3,58,mode='s').finalize().extrude(-62))