import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,26,0))
w1=cq.Workplane('ZX',origin=(0,19,0))
r=w0.sketch().segment((-30,28),(-10,28)).segment((39,76)).arc((10,70),(-7,46)).segment((-30,46)).close().assemble().finalize().extrude(-53).union(w1.sketch().segment((-54,-100),(50,-100)).segment((50,-56)).arc((21,-47),(-1,-24)).arc((32,91),(-54,7)).close().assemble().push([(-37,-7)]).circle(16,mode='s').finalize().extrude(-18))