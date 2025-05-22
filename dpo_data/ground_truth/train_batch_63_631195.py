import cadquery as cq
w0=cq.Workplane('YZ',origin=(80,0,0))
w1=cq.Workplane('YZ',origin=(77,0,0))
r=w0.sketch().arc((38,46),(6,-81),(78,29)).segment((98,43)).segment((77,73)).close().assemble().push([(32.5,-19.5)]).rect(35,119,mode='s').finalize().extrude(-126).union(w1.sketch().segment((-2,-25),(-2,-2)).segment((17,-2)).arc((-87,63),(-2,-25)).assemble().finalize().extrude(-158))