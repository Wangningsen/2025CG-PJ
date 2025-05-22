import cadquery as cq
w0=cq.Workplane('YZ',origin=(11,0,0))
r=w0.sketch().push([(34,0)]).circle(66).circle(56,mode='s').finalize().extrude(-22).union(w0.workplane(offset=-8/2).moveTo(-60,-28).box(80,70,8))