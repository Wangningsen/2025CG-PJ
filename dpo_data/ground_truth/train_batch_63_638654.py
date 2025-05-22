import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,42))
w1=cq.Workplane('YZ',origin=(-21,0,0))
r=w0.sketch().segment((2,4),(2,16)).segment((11,16)).arc((-60,50),(4,4)).close().assemble().finalize().extrude(17).union(w0.workplane(offset=58/2).moveTo(-25.5,29.5).box(95,75,58)).union(w1.sketch().arc((-46,1),(-61,-82),(23,-77)).arc((70,-43),(63,14)).arc((57,30),(47,44)).segment((47,54)).segment((31,54)).arc((8,59),(-14,54)).segment((-30,54)).segment((-30,44)).arc((-43,24),(-46,1)).assemble().finalize().extrude(94))