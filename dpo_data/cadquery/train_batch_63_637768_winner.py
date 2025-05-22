import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-80,0))
w1=cq.Workplane('YZ',origin=(-92,0,0))
r=w0.workplane(offset=180/2).moveTo(0,-28).cylinder(180,33).union(w1.sketch().push([(-23,0)]).rect(154,52).reset().face(w1.sketch().segment((-45,-13),(-33,-13)).arc((-23,-16),(-12,-13)).segment((-1,-13)).segment((-1,13)).segment((-12,13)).arc((-23,16),(-33,13)).segment((-45,13)).close().assemble(),mode='s').finalize().extrude(184))