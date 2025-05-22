import cadquery as cq
w0=cq.Workplane('YZ',origin=(-25,0,0))
r=w0.sketch().push([(-4,-1)]).rect(52,60).push([(-4,-10.5)]).rect(50,5,mode='s').push([(-4,0)]).rect(50,22,mode='s').finalize().extrude(-75).union(w0.workplane(offset=125/2).cylinder(125,58))