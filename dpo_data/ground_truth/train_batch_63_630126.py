import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-60,0))
r=w0.workplane(offset=-40/2).cylinder(40,85).union(w0.sketch().arc((12,-10),(7,-4),(14,-7)).arc((-13,9),(12,-10)).assemble().circle(7,mode='s').finalize().extrude(160))