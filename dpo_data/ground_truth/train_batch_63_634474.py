import cadquery as cq
w0=cq.Workplane('YZ',origin=(7,0,0))
w1=cq.Workplane('XY',origin=(0,0,-32))
r=w0.workplane(offset=53/2).moveTo(40,-61).cylinder(53,32).union(w0.workplane(offset=56/2).moveTo(-57,50).cylinder(56,43)).union(w1.sketch().arc((-31,45),(-80,-19),(-11,21)).segment((-8,21)).segment((-8,14)).segment((12,14)).segment((12,2)).segment((-8,2)).segment((-8,-20)).segment((22,-20)).arc((36,32),(90,38)).segment((90,59)).segment((66,59)).segment((66,100)).segment((-8,100)).segment((-8,59)).segment((-31,59)).close().assemble().finalize().extrude(-7))