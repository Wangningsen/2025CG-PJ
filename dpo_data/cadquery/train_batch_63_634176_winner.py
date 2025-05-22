import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-34))
r=w0.workplane(offset=-49/2).moveTo(-48,-23).cylinder(49,50).union(w0.workplane(offset=-22/2).moveTo(50.5,-14).box(99,92,22)).union(w0.sketch().segment((40,-21),(84,-21)).segment((84,-7)).segment((43,-7)).arc((-99,14),(40,-21)).assemble().finalize().extrude(116))