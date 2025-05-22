import cadquery as cq
w0=cq.Workplane('YZ',origin=(23,0,0))
w1=cq.Workplane('YZ',origin=(-23,0,0))
r=w0.sketch().push([(-41,45)]).circle(11).push([(48,-4)]).circle(52).push([(48,-3.5)]).rect(18,87,mode='s').finalize().extrude(-35).union(w1.workplane(offset=4/2).moveTo(-62.5,51.5).box(75,5,4))