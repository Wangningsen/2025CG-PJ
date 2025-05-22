import cadquery as cq
w0=cq.Workplane('YZ',origin=(-46,0,0))
w1=cq.Workplane('XY',origin=(0,0,27))
r=w0.sketch().segment((-33,-59),(-25,-59)).segment((-25,-60)).segment((66,-60)).segment((66,-59)).segment((74,-59)).segment((74,59)).segment((66,59)).segment((66,60)).segment((-25,60)).segment((-25,59)).segment((-33,59)).close().assemble().finalize().extrude(146).union(w1.sketch().arc((-100,-56),(-100,-57),(-99,-57)).arc((-96,-57),(-97,-60)).arc((-91,-67),(-87,-74)).arc((-78,-54),(-100,-56)).assemble().finalize().extrude(-11))