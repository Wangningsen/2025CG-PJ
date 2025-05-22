import cadquery as cq
w0=cq.Workplane('YZ',origin=(-38,0,0))
w1=cq.Workplane('YZ',origin=(37,0,0))
r=w0.sketch().rect(200,14).circle(3,mode='s').finalize().extrude(57).union(w1.workplane(offset=-75/2).cylinder(75,100))