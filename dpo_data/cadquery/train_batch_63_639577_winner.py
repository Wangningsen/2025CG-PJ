import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-93,0))
r=w0.sketch().segment((-100,-69),(100,-69)).segment((100,-64)).segment((-14,-64)).segment((-14,-42)).segment((44,-42)).arc((47,-40),(50,-42)).segment((100,-42)).segment((100,69)).segment((-100,69)).close().assemble().finalize().extrude(185)