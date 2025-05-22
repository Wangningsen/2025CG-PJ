import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-9,0))
r=w0.sketch().segment((-81,-47),(5,-100)).segment((81,18)).segment((42,42)).segment((60,71)).segment((10,100)).segment((-11,61)).segment((-5,58)).segment((-81,-29)).segment((-68,-40)).close().assemble().finalize().extrude(18)