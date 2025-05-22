import cadquery as cq
w0=cq.Workplane('YZ',origin=(92,0,0))
r=w0.workplane(offset=-184/2).cylinder(184,100)