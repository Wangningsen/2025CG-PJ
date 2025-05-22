import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,22,0))
w1=cq.Workplane('ZX',origin=(0,25,0))
r=w0.sketch().segment((69,-73),(89,-73)).segment((89,30)).segment((85,30)).arc((79,4),(69,-17)).close().assemble().finalize().extrude(-45).union(w1.sketch().arc((-85,-8),(-63,-97),(5,-31)).arc((12,-20),(15,-7)).arc((17,-6),(20,-6)).arc((25,-5),(29,-4)).arc((97,57),(9,86)).arc((0,73),(-7,86)).arc((-80,67),(-85,-8)).assemble().finalize().extrude(-50))