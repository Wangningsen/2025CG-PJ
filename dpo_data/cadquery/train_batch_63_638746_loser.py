import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-52))
r=w0.sketch().segment((-90,2),(-74,1)).segment((-74,-20)).segment((-3,-20)).segment((-3,3)).segment((7,3)).segment((12,77)).segment((-3,78)).segment((-3,100)).segment((-74,100)).segment((-74,77)).segment((-83,77)).close().assemble().finalize().extrude(96).union(w0.workplane(offset=104/2).moveTo(35.5,-42).box(109,116,104))