import cadquery as cq
w0=cq.Workplane('YZ',origin=(30,0,0))
r=w0.sketch().rect(152,200).rect(98,130,mode='s').finalize().extrude(-69).union(w0.workplane(offset=9/2).cylinder(9,11))