import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-59))
r=w0.workplane(offset=6/2).moveTo(52,68).cylinder(6,32).union(w0.sketch().segment((-16,-96),(-16,-69)).segment((59,-69)).arc((36,-56),(12,-60)).arc((-73,-22),(-16,-96)).assemble().finalize().extrude(118))