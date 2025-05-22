import cadquery as cq
w0=cq.Workplane('YZ',origin=(31,0,0))
w1=cq.Workplane('YZ',origin=(0,0,0))
r=w0.sketch().push([(93,0)]).rect(14,24).circle(2,mode='s').finalize().extrude(34).union(w1.sketch().push([(-43,0)]).circle(57).push([(1,12)]).circle(7,mode='s').finalize().extrude(-65))