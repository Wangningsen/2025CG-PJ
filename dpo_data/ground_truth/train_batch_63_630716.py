import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-59))
r=w0.sketch().arc((-14,-67),(-15,-64),(-12,-63)).arc((-58,-39),(-14,-67)).assemble().push([(52,68)]).circle(32).finalize().extrude(6).union(w0.sketch().segment((-16,-96),(-16,-69)).segment((59,-69)).arc((37,-56),(12,-60)).arc((-74,-23),(-16,-96)).assemble().finalize().extrude(118))