import cadquery as cq
w0=cq.Workplane('YZ',origin=(37,0,0))
r=w0.workplane(offset=-75/2).cylinder(75,100)