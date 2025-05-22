import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-3))
r=w0.sketch().segment((14,-3),(80,-3)).segment((80,3)).segment((69,3)).arc((68,1),(67,3)).segment((14,3)).close().assemble().finalize().extrude(-97).union(w0.workplane(offset=103/2).moveTo(-43,0).box(74,44,103))