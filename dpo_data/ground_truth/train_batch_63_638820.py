import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-26))
w1=cq.Workplane('ZX',origin=(0,37,0))
r=w0.sketch().push([(-49,8)]).circle(51).reset().face(w0.sketch().arc((20,6),(27,-3),(36,-11)).segment((36,-31)).segment((89,-31)).segment((89,1)).arc((78,57),(22,46)).arc((14,28),(29,40)).arc((35,20),(20,6)).assemble()).finalize().extrude(46).union(w0.workplane(offset=52/2).moveTo(56,24).box(88,94,52)).union(w1.sketch().arc((-21,34),(-11,56),(-21,78)).close().assemble().finalize().extrude(-108))