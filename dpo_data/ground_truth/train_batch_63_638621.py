import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,8,0))
r=w0.workplane(offset=-83/2).moveTo(42.5,24.5).box(21,17,83).union(w0.sketch().push([(-88,-96)]).circle(4).push([(42,50)]).circle(50).finalize().extrude(66))