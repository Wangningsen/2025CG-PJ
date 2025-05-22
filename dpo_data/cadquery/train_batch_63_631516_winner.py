import cadquery as cq
w0=cq.Workplane('YZ',origin=(-53,0,0))
r=w0.sketch().push([(58,-80)]).circle(20).push([(71,-88)]).circle(2,mode='s').finalize().extrude(99).union(w0.workplane(offset=107/2).moveTo(-22.5,41).box(111,118,107))