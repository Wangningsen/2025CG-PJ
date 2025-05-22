import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-82,0))
r=w0.workplane(offset=165/2).box(200,36,165)