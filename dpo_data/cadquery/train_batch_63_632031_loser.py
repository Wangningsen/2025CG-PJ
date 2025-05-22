import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-47))
r=w0.sketch().segment((-12,-11),(32,15)).segment((63,-32)).segment((23,-55)).arc((85,39),(-12,-11)).assemble().finalize().extrude(-16).union(w0.workplane(offset=111/2).moveTo(-90.5,-0.5).box(19,51,111))