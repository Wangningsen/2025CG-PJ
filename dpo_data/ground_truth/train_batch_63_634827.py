import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().segment((-95,24),(76,-62)).segment((95,-24)).segment((-76,62)).close().assemble().finalize().extrude(-200).union(w0.sketch().rect(72,132).circle(17,mode='s').finalize().extrude(-12))