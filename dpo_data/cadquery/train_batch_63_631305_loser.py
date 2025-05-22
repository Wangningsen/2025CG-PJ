import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().rect(190,40).push([(-21,-7)]).circle(2,mode='s').finalize().extrude(-200).union(w0.workplane(offset=-98/2).cylinder(98,56))