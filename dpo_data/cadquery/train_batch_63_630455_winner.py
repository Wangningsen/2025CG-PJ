import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-58,0))
r=w0.workplane(offset=18/2).moveTo(26,10.5).box(108,123,18).union(w0.sketch().segment((-100,4),(-35,-72)).segment((-7,-49)).segment((65,-49)).segment((65,-44)).arc((100,1),(65,46)).segment((65,71)).segment((-12,71)).segment((-12,-2)).segment((-52,45)).close().assemble().finalize().extrude(116))