import cadquery as cq
w0=cq.Workplane('YZ',origin=(37,0,0))
w1=cq.Workplane('YZ',origin=(36,0,0))
r=w0.sketch().rect(122,200).circle(14,mode='s').finalize().extrude(-73).union(w1.workplane(offset=-24/2).cylinder(24,54))