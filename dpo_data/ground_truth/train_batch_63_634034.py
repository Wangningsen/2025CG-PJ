import cadquery as cq
w0=cq.Workplane('YZ',origin=(-28,0,0))
w1=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().segment((-41,-16),(-28,-31)).segment((-17,-22)).segment((-30,-7)).arc((-35,-12),(-41,-16)).assemble().finalize().extrude(-55).union(w0.workplane(offset=126/2).moveTo(-56,13).cylinder(126,17)).union(w1.workplane(offset=200/2).moveTo(0,-94).box(120,8,200))