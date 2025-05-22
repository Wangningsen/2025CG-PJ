import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().segment((-56,-22),(-18,-22)).arc((0,-29),(18,-22)).segment((56,-22)).segment((56,22)).segment((18,22)).arc((0,29),(-18,22)).segment((-56,22)).close().assemble().finalize().extrude(-200).union(w0.workplane(offset=-11/2).box(24,62,11))