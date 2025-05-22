import cadquery as cq
w0=cq.Workplane('YZ',origin=(-3,0,0))
r=w0.sketch().arc((-91,-40),(-60,-45),(-69,-76)).segment((-68,-93)).arc((-42,-100),(-15,-97)).segment((-14,-97)).arc((79,60),(-91,-40)).assemble().finalize().extrude(6)