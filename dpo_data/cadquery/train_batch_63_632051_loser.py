import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-21))
r=w0.workplane(offset=-79/2).cylinder(79,54).union(w0.sketch().segment((-29,-18),(29,-18)).arc((0,34),(-29,-18)).assemble().finalize().extrude(121))