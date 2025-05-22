import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-59))
r=w0.workplane(offset=6/2).moveTo(52,69).cylinder(6,31).union(w0.sketch().segment((-16,-96),(-16,-69)).segment((59,-69)).arc((39,-57),(16,-57)).arc((-76,-25),(-16,-96)).assemble().finalize().extrude(118))