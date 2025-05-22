import cadquery as cq
w0=cq.Workplane('YZ',origin=(-15,0,0))
w1=cq.Workplane('YZ',origin=(-16,0,0))
r=w0.workplane(offset=-2/2).moveTo(36,-9).cylinder(2,44).union(w0.sketch().arc((17,21),(-100,-3),(19,-25)).segment((19,-43)).segment((21,-43)).arc((57,8),(87,-43)).segment((100,-43)).segment((100,21)).segment((56,21)).segment((56,63)).segment((52,63)).segment((52,21)).close().assemble().finalize().extrude(32)).union(w1.sketch().segment((5,-32),(6,-32)).segment((6,-34)).arc((13,-30),(5,-32)).assemble().finalize().extrude(32))