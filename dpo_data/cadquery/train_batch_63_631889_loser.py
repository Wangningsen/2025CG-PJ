import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-16,0))
w1=cq.Workplane('ZX',origin=(0,-40,0))
r=w0.workplane(offset=-84/2).moveTo(-41,-15).cylinder(84,17).union(w0.sketch().segment((52,-6),(53,-12)).segment((58,-12)).segment((57,-6)).close().assemble().finalize().extrude(-84)).union(w1.workplane(offset=140/2).moveTo(-32,30).cylinder(140,2))