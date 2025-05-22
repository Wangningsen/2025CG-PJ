import cadquery as cq
w0=cq.Workplane('YZ',origin=(80,0,0))
r=w0.sketch().segment((-100,3),(-78,3)).arc((-68,-14),(-52,-25)).segment((-52,-64)).segment((100,-64)).segment((100,-22)).segment((-11,-22)).arc((2,-11),(10,3)).segment((31,3)).segment((31,32)).segment((10,32)).arc((-34,64),(-78,32)).segment((-100,32)).close().assemble().push([(76.5,-24.5)]).rect(3,3,mode='s').finalize().extrude(-161)