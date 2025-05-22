import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().rect(104,130).push([(19,-28)]).rect(52,8,mode='s').push([(16.5,44.5)]).rect(9,9,mode='s').finalize().extrude(-200)