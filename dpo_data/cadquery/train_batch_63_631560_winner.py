import cadquery as cq
w0=cq.Workplane('YZ',origin=(-8,0,0))
w1=cq.Workplane('ZX',origin=(0,14,0))
r=w0.sketch().segment((-100,-22),(-62,-45)).segment((-40,-7)).segment((-78,15)).close().assemble().reset().face(w0.sketch().arc((-16,-21),(-2,-74),(35,-35)).arc((30,-6),(-1,-3)).segment((-7,6)).close().assemble()).finalize().extrude(68).union(w1.sketch().push([(50.5,-39.5)]).rect(49,41).rect(35,9,mode='s').finalize().extrude(86))