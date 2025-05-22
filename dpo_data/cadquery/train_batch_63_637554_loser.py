import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-92,0))
w1=cq.Workplane('YZ',origin=(-41,0,0))
r=w0.workplane(offset=184/2).moveTo(0,-74).cylinder(184,26).union(w1.workplane(offset=141/2).moveTo(-75,0).cylinder(141,7))