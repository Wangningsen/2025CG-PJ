import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-47))
r=w0.sketch().segment((-14,-12),(38,15)).segment((62,-33)).segment((23,-54)).arc((85,39),(-14,-12)).assemble().finalize().extrude(-17).union(w0.workplane(offset=111/2).moveTo(-90.5,-0.5).box(19,51,111))