import cadquery as cq
w0=cq.Workplane('YZ',origin=(-68,0,0))
r=w0.sketch().push([(95,-82)]).circle(5).circle(2,mode='s').finalize().extrude(62).union(w0.workplane(offset=136/2).moveTo(-48.5,67).box(103,40,136))