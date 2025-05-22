import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-17,0))
r=w0.sketch().segment((-100,-32),(-89,-32)).arc((-46,-53),(-4,-32)).segment((7,-32)).segment((7,32)).segment((-4,32)).arc((-46,53),(-89,32)).segment((-100,32)).close().assemble().finalize().extrude(-54).union(w0.sketch().push([(76,-10)]).circle(24).rect(20,40,mode='s').finalize().extrude(88))