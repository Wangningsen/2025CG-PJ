import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,65))
r=w0.sketch().segment((52,68),(55,71)).segment((57,70)).arc((16,86),(55,66)).close().assemble().push([(23,81)]).circle(4,mode='s').finalize().extrude(-130).union(w0.workplane(offset=-114/2).moveTo(0,-12).cylinder(114,88))