import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-26))
w1=cq.Workplane('ZX',origin=(0,18,0))
r=w0.workplane(offset=46/2).moveTo(-49,8).cylinder(46,51).union(w0.sketch().segment((12,-23),(36,-23)).segment((36,-31)).segment((89,-31)).segment((89,-23)).segment((100,-23)).segment((100,71)).segment((12,71)).close().assemble().finalize().extrude(52)).union(w1.sketch().arc((-21,34),(-12,56),(-21,78)).close().assemble().finalize().extrude(-89))