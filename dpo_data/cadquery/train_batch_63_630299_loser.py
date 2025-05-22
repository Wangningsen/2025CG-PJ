import cadquery as cq
w0=cq.Workplane('YZ',origin=(-12,0,0))
w1=cq.Workplane('YZ',origin=(12,0,0))
r=w0.sketch().push([(43,-98)]).circle(2).push([(43,-98.5)]).rect(2,1,mode='s').finalize().extrude(24).union(w1.workplane(offset=-25/2).moveTo(-4,58).cylinder(25,42))