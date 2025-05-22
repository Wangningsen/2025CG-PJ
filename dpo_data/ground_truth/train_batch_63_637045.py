import cadquery as cq
w0=cq.Workplane('YZ',origin=(63,0,0))
r=w0.workplane(offset=-126/2).moveTo(38,0).box(124,104,126).union(w0.sketch().push([(-92,-35)]).circle(8).circle(7,mode='s').finalize().extrude(-13))