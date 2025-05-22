import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-74,0))
r=w0.sketch().segment((-100,-86),(-95,-86)).segment((-95,-88)).segment((-99,-88)).arc((-93,-83),(-100,-86)).assemble().finalize().extrude(-14).union(w0.workplane(offset=162/2).moveTo(36,25).cylinder(162,64))