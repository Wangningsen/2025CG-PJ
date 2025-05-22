import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,61,0))
r=w0.sketch().segment((-89,-63),(-77,-63)).arc((0,-100),(77,-63)).segment((89,-63)).segment((89,-45)).arc((100,0),(89,45)).segment((89,63)).segment((77,63)).arc((0,100),(-77,63)).segment((-89,63)).segment((-89,45)).arc((-100,0),(-89,-45)).close().assemble().finalize().extrude(-123)