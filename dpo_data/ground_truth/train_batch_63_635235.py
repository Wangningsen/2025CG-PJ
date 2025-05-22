import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,39))
r=w0.sketch().segment((-44,75),(-38,17)).arc((-69,-76),(-26,12)).segment((15,16)).segment((8,80)).close().assemble().push([(-31,25)]).circle(2,mode='s').finalize().extrude(-83).union(w0.workplane(offset=6/2).moveTo(99.5,-56.5).box(1,25,6))