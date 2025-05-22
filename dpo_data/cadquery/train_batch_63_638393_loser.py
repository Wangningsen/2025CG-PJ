import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-38,0))
r=w0.sketch().segment((-98,-96),(-88,-99)).segment((-79,-74)).arc((-1,-84),(32,-14)).segment((100,-14)).segment((100,99)).segment((-92,99)).segment((-92,8)).arc((-100,-25),(-89,-60)).close().assemble().push([(4,42)]).rect(96,80,mode='s').finalize().extrude(76)