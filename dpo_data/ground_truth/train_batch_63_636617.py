import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,4,0))
w1=cq.Workplane('YZ',origin=(39,0,0))
r=w0.sketch().segment((62,-83),(66,-83)).segment((66,-71)).arc((52,-100),(65,-70)).segment((62,-70)).segment((62,-72)).arc((53,-75),(62,-79)).close().assemble().finalize().extrude(-79).union(w1.sketch().arc((-28,54),(-48,-62),(61,-17)).arc((53,65),(-28,54)).assemble().finalize().extrude(61))