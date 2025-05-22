import cadquery as cq
w0=cq.Workplane('YZ',origin=(-71,0,0))
w1=cq.Workplane('ZX',origin=(0,-92,0))
r=w0.sketch().segment((-80,-2),(-70,-4)).segment((-69,4)).arc((-76,-7),(-78,6)).close().assemble().finalize().extrude(171).union(w1.workplane(offset=184/2).moveTo(0,-74).cylinder(184,26))