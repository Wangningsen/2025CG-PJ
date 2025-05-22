import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.workplane(offset=193/2).box(72,30,193).union(w0.sketch().circle(15).circle(6,mode='s').finalize().extrude(200))