import cadquery as cq
w0=cq.Workplane('YZ',origin=(46,0,0))
r=w0.workplane(offset=-92/2).box(22,200,92)