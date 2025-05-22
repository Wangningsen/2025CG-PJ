import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-1,0))
r=w0.sketch().arc((-45,-32),(-1,-76),(59,-62)).arc((97,15),(17,52)).arc((8,55),(-1,56)).arc((-93,50),(-45,-32)).assemble().reset().face(w0.sketch().arc((-40,-30),(-1,-64),(46,-50)).arc((-1,-50),(-40,-30)).assemble(),mode='s').finalize().extrude(2)