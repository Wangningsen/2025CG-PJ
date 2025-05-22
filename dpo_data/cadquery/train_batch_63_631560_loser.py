import cadquery as cq
w0=cq.Workplane('YZ',origin=(-8,0,0))
w1=cq.Workplane('ZX',origin=(0,14,0))
r=w0.sketch().segment((-100,-22),(-64,-44)).segment((-41,-10)).segment((-76,14)).close().assemble().reset().face(w0.sketch().arc((-21,-28),(-2,-74),(36,-42)).arc((26,-3),(-15,-17)).arc((-19,-24),(-21,-28)).assemble()).finalize().extrude(68).union(w1.sketch().push([(50.5,-39.5)]).rect(49,41).rect(37,9,mode='s').finalize().extrude(86))