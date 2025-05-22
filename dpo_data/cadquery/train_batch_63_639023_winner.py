import cadquery as cq
w0=cq.Workplane('YZ',origin=(-55,0,0))
w1=cq.Workplane('YZ',origin=(-65,0,0))
r=w0.sketch().push([(45,0)]).circle(55).push([(79,39)]).circle(2,mode='s').finalize().extrude(120).union(w1.workplane(offset=44/2).moveTo(-55,1.5).box(90,67,44))