import cadquery as cq
w0=cq.Workplane('YZ',origin=(61,0,0))
w1=cq.Workplane('XY',origin=(0,0,-3))
r=w0.workplane(offset=-41/2).moveTo(-8,-42).box(16,116,41).union(w0.sketch().push([(0,32)]).circle(68).push([(2,81)]).circle(12,mode='s').finalize().extrude(-20)).union(w1.sketch().segment((-61,52),(-39,52)).arc((-50,56),(-61,52)).assemble().finalize().extrude(-45))