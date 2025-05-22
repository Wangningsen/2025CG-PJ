import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,66,0))
r=w0.workplane(offset=-133/2).moveTo(36,-64).cylinder(133,36).union(w0.sketch().arc((-24,79),(-71,42),(-13,32)).arc((24,28),(46,57)).segment((58,59)).segment((55,81)).segment((43,79)).arc((9,100),(-24,79)).assemble().finalize().extrude(-19))