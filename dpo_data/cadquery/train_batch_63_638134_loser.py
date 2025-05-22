import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-42,0))
w1=cq.Workplane('ZX',origin=(0,-37,0))
r=w0.sketch().segment((-72,-41),(-23,-82)).segment((-23,-100)).segment((3,-100)).segment((3,-72)).segment((44,-21)).segment((32,-12)).arc((-10,-47),(-61,-48)).arc((-66,-46),(-69,-43)).close().assemble().reset().face(w0.sketch().arc((32,19),(35,6),(35,-8)).segment((44,-22)).arc((40,4),(32,19)).assemble()).finalize().extrude(-4).union(w1.sketch().segment((-4,68),(72,68)).arc((34,100),(-4,68)).assemble().finalize().extrude(83))