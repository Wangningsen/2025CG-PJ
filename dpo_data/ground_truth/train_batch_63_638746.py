import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-51))
r=w0.sketch().segment((-90,2),(-74,1)).segment((-74,-20)).segment((-3,-20)).segment((-3,-5)).segment((6,-6)).segment((12,77)).segment((-3,79)).segment((-3,100)).segment((-74,100)).segment((-74,85)).segment((-83,85)).close().assemble().finalize().extrude(95).union(w0.workplane(offset=103/2).moveTo(35.5,-42).box(109,116,103))