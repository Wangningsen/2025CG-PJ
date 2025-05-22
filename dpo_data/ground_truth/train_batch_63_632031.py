import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-46))
r=w0.sketch().segment((-14,-12),(36,15)).segment((62,-33)).segment((23,-54)).arc((86,38),(-14,-12)).assemble().finalize().extrude(-17).union(w0.workplane(offset=110/2).moveTo(-90.5,0).box(19,52,110))