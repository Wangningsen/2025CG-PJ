import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-39,0))
w1=cq.Workplane('YZ',origin=(-67,0,0))
r=w0.workplane(offset=129/2).moveTo(-64,31).cylinder(129,36).union(w1.sketch().arc((-71,-6),(-81,-33),(-70,-59)).arc((-74,-68),(-65,-66)).arc((-12,-65),(-1,-11)).arc((-24,100),(-71,-6)).assemble().finalize().extrude(104))