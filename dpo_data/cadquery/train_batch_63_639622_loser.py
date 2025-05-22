import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.workplane(offset=105/2).moveTo(4,-31).cylinder(105,41).union(w0.sketch().push([(27.5,56.5)]).rect(97,39).push([(9,72)]).circle(1,mode='s').finalize().extrude(154)).union(w0.sketch().segment((-76,-76),(-65,-76)).arc((-66,-57),(-63,-39)).segment((-76,-39)).close().assemble().finalize().extrude(200))