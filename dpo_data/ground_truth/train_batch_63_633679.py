import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-64))
r=w0.workplane(offset=42/2).cylinder(42,29).union(w0.workplane(offset=53/2).moveTo(51,-7).cylinder(53,45)).union(w0.sketch().segment((-100,-23),(48,-91)).segment((100,23)).segment((-48,91)).close().assemble().finalize().extrude(127))