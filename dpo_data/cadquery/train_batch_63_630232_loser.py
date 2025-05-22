import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-50,0))
r=w0.sketch().push([(96.5,-87.5)]).rect(7,19).push([(96,-87)]).circle(2,mode='s').finalize().extrude(40).union(w0.sketch().segment((-100,-40),(-29,-40)).segment((-29,-98)).segment((-4,-98)).segment((-4,-40)).segment((34,-40)).segment((34,98)).segment((-100,98)).close().assemble().finalize().extrude(100))