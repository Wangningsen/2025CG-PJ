import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-13,0))
w1=cq.Workplane('YZ',origin=(-27,0,0))
r=w0.sketch().segment((-94,-3),(-84,-3)).segment((-84,-10)).segment((-92,-10)).arc((-39,13),(-94,-3)).assemble().finalize().extrude(-33).union(w1.sketch().arc((-42,50),(-88,-25),(-8,6)).segment((16,6)).segment((16,-53)).segment((100,-53)).segment((100,32)).segment((68,32)).segment((68,50)).segment((57,50)).segment((57,94)).segment((-42,94)).close().assemble().push([(-20.5,45)]).rect(19,14,mode='s').push([(-20.5,49)]).rect(19,6,mode='s').finalize().extrude(56))