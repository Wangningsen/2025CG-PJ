import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,4))
r=w0.workplane(offset=-15/2).moveTo(87.5,-55.5).box(25,23,15).union(w0.sketch().push([(-33.5,15)]).rect(133,104).push([(-80.5,44)]).rect(25,20,mode='s').finalize().extrude(7))