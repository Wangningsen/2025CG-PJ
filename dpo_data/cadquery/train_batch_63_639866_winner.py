import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,62,0))
w1=cq.Workplane('XY',origin=(0,0,-10))
r=w0.workplane(offset=-60/2).moveTo(69,-81).cylinder(60,19).union(w0.sketch().arc((88,59),(95,78),(88,95)).close().assemble().finalize().extrude(-49)).union(w1.sketch().push([(83,-45)]).circle(17).circle(8,mode='s').finalize().extrude(-85))