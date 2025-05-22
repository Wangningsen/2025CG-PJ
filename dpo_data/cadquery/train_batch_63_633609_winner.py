import cadquery as cq
w0=cq.Workplane('YZ',origin=(-8,0,0))
r=w0.sketch().circle(16).circle(10,mode='s').finalize().extrude(-92).union(w0.sketch().circle(74).push([(-18.5,58)]).rect(33,24,mode='s').finalize().extrude(108))