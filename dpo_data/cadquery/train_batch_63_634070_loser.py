import cadquery as cq
w0=cq.Workplane('YZ',origin=(-25,0,0))
r=w0.sketch().push([(-4,0)]).rect(52,62).rect(50,24,mode='s').finalize().extrude(-75).union(w0.workplane(offset=125/2).cylinder(125,58))