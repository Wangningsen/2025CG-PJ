import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().rect(190,40).push([(-18,-5)]).circle(3,mode='s').finalize().extrude(-200).union(w0.workplane(offset=-98/2).cylinder(98,56))