import cadquery as cq
w0=cq.Workplane('YZ',origin=(12,0,0))
w1=cq.Workplane('XY',origin=(0,0,9))
r=w0.workplane(offset=-44/2).moveTo(32,31).cylinder(44,30).union(w0.sketch().segment((14,34),(29,34)).arc((32,35),(34,34)).segment((49,34)).arc((32,49),(14,34)).assemble().finalize().extrude(26)).union(w1.sketch().segment((-82,-91),(-22,-91)).segment((-22,-78)).arc((-4,-40),(-22,-3)).segment((-22,5)).arc((94,55),(-24,11)).segment((-82,11)).segment((-82,-3)).arc((-100,-40),(-82,-78)).close().assemble().finalize().extrude(-71))