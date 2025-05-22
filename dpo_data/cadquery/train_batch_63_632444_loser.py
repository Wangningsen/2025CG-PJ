import cadquery as cq
w0=cq.Workplane('YZ',origin=(16,0,0))
w1=cq.Workplane('YZ',origin=(16,0,0))
r=w0.sketch().rect(200,200).push([(75,11)]).circle(11,mode='s').finalize().extrude(-31).union(w1.workplane(offset=-31/2).box(158,192,31))