import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().segment((-95,24),(76,-62)).segment((95,-24)).segment((-76,62)).close().assemble().finalize().extrude(-200).union(w0.sketch().rect(72,132).push([(-34,-56)]).circle(2,mode='s').push([(-3,-1)]).circle(24,mode='s').finalize().extrude(-12))