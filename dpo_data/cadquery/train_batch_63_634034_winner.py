import cadquery as cq
w0=cq.Workplane('YZ',origin=(-28,0,0))
w1=cq.Workplane('YZ',origin=(-98,0,0))
r=w0.sketch().segment((-41,-16),(-28,-31)).segment((-17,-22)).segment((-30,-7)).close().assemble().finalize().extrude(-57).union(w0.workplane(offset=126/2).moveTo(-56,13).cylinder(126,17)).union(w1.workplane(offset=8/2).box(200,120,8))