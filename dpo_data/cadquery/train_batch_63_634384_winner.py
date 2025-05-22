import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-49))
r=w0.workplane(offset=95/2).moveTo(-32,-71).cylinder(95,29).union(w0.sketch().segment((-32,13),(-32,19)).segment((-16,19)).segment((-16,9)).segment((-28,9)).arc((16,-9),(49,20)).arc((30,97),(-36,45)).arc((-37,30),(-32,13)).assemble().finalize().extrude(98))