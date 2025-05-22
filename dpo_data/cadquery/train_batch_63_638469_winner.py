import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,50,0))
r=w0.workplane(offset=-101/2).cylinder(101,100)