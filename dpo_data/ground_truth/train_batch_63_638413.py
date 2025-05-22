import cadquery as cq
w0=cq.Workplane('YZ',origin=(-2,0,0))
r=w0.sketch().segment((-50,27),(-48,27)).arc((-35,9),(-17,-2)).arc((0,-100),(17,-2)).arc((35,9),(48,27)).segment((50,27)).segment((50,34)).arc((52,48),(50,61)).segment((50,68)).segment((48,68)).arc((0,100),(-48,68)).segment((-50,68)).segment((-50,61)).arc((-52,48),(-50,34)).close().assemble().finalize().extrude(4)