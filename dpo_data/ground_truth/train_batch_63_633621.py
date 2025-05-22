import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-41,0))
r=w0.sketch().arc((-100,25),(-80,-2),(-96,-31)).arc((-55,0),(-100,25)).assemble().finalize().extrude(-6).union(w0.workplane(offset=88/2).moveTo(45,0).cylinder(88,55))