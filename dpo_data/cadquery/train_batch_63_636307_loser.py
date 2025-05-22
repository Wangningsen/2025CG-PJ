import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,10,0))
r=w0.workplane(offset=-20/2).box(174,200,20)