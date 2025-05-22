import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-3))
r=w0.sketch().segment((14,-3),(57,-3)).arc((58,1),(59,-3)).segment((80,-3)).segment((80,3)).segment((14,3)).close().assemble().push([(40,0)]).circle(1,mode='s').finalize().extrude(-97).union(w0.workplane(offset=103/2).moveTo(-43,0).box(74,44,103))