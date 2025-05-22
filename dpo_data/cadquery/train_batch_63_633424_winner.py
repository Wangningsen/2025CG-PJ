import cadquery as cq
w0=cq.Workplane('YZ',origin=(-69,0,0))
r=w0.workplane(offset=6/2).box(156,160,6).union(w0.sketch().circle(100).circle(92,mode='s').finalize().extrude(139))