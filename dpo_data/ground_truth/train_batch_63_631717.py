import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().push([(-23,-4)]).rect(124,186).circle(53,mode='s').finalize().extrude(143).union(w0.workplane(offset=200/2).moveTo(0,12).cylinder(200,85))