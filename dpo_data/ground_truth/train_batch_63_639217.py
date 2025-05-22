import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,3))
r=w0.workplane(offset=-14/2).moveTo(87.5,-55.5).box(25,23,14).union(w0.sketch().push([(-33.5,15)]).rect(133,104).push([(-79,44)]).circle(11,mode='s').finalize().extrude(7))