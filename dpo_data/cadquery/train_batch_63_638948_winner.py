import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,1))
r=w0.workplane(offset=-98/2).moveTo(-74,-71).cylinder(98,26).union(w0.sketch().segment((-74,61),(100,61)).segment((100,97)).segment((-74,97)).segment((-74,80)).arc((-67,73),(-74,65)).close().assemble().push([(-74,-72)]).circle(11).finalize().extrude(96))