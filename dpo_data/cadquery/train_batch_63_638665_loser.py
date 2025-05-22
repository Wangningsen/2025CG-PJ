import cadquery as cq
w0=cq.Workplane('YZ',origin=(-56,0,0))
r=w0.sketch().segment((-15,34),(40,-7)).arc((26,26),(-10,37)).segment((-10,34)).close().assemble().finalize().extrude(-44).union(w0.sketch().arc((45,-33),(47,-31),(48,-29)).arc((-47,23),(52,22)).arc((48,23),(44,21)).arc((-45,2),(45,-29)).close().assemble().finalize().extrude(156))