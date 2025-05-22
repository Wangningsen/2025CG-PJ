import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-25,0))
w1=cq.Workplane('YZ',origin=(-38,0,0))
r=w0.workplane(offset=104/2).moveTo(-54,-51).cylinder(104,5).union(w0.workplane(offset=107/2).moveTo(52,8).cylinder(107,48)).union(w1.workplane(offset=58/2).moveTo(-55,-73).cylinder(58,27))