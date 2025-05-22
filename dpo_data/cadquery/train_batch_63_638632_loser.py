import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,48,0))
w1=cq.Workplane('YZ',origin=(13,0,0))
r=w0.sketch().segment((-30,-100),(27,-100)).segment((27,-46)).arc((33,-34),(27,-22)).segment((27,4)).segment((-30,4)).close().assemble().reset().face(w0.sketch().segment((-28,-67),(26,-67)).segment((26,-47)).arc((2,-34),(27,-22)).segment((27,-19)).segment((20,-19)).arc((15,-18),(11,-19)).segment((-28,-19)).close().assemble(),mode='s').finalize().extrude(-99).union(w1.workplane(offset=87/2).moveTo(29,-11).cylinder(87,22))