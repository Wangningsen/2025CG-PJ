import cadquery as cq
w0=cq.Workplane('YZ',origin=(-42,0,0))
r=w0.sketch().push([(75,35)]).rect(22,130).circle(3,mode='s').push([(84,-14)]).circle(2,mode='s').finalize().extrude(-4).union(w0.workplane(offset=89/2).moveTo(-77,-36.5).box(18,127,89))