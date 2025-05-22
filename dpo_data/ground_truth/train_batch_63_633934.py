import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,36,0))
w1=cq.Workplane('XY',origin=(0,0,53))
r=w0.sketch().arc((-3,47),(-96,-31),(26,-32)).arc((97,38),(-3,47)).assemble().reset().face(w0.sketch().arc((9,38),(24,17),(30,-8)).segment((81,-8)).segment((81,46)).segment((9,46)).close().assemble(),mode='s').finalize().extrude(-126).union(w0.workplane(offset=-111/2).moveTo(45,19).cylinder(111,34)).union(w1.workplane(offset=-49/2).moveTo(-26,73).box(60,34,49))