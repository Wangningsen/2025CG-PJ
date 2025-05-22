import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,79))
w1=cq.Workplane('XY',origin=(0,0,50))
r=w0.workplane(offset=13/2).moveTo(11,-67).cylinder(13,33).union(w1.sketch().arc((-45,16),(-27,4),(-12,-7)).arc((27,93),(-45,16)).assemble().finalize().extrude(-142))