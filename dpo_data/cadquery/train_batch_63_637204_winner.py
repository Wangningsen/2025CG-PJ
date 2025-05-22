import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,50))
w1=cq.Workplane('XY',origin=(0,0,79))
r=w0.sketch().arc((-40,10),(-26,3),(-14,-6)).arc((29,92),(-40,10)).assemble().finalize().extrude(-142).union(w1.workplane(offset=13/2).moveTo(12,-67).cylinder(13,33))