import cadquery as cq
w0=cq.Workplane('YZ',origin=(76,0,0))
w1=cq.Workplane('XY',origin=(0,0,52))
r=w0.sketch().segment((-11,-1),(-11,100)).arc((-38,49),(-11,-1)).assemble().finalize().extrude(-168).union(w1.workplane(offset=-152/2).moveTo(76,22).cylinder(152,16))