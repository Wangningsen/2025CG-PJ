import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,43))
r=w0.workplane(offset=-99/2).moveTo(-64,-63).cylinder(99,31).union(w0.sketch().arc((-100,10),(-91,-18),(-68,-33)).arc((-29,-61),(14,-43)).segment((14,-48)).segment((100,-48)).segment((100,40)).segment((54,40)).segment((54,94)).segment((-42,94)).segment((-42,50)).arc((-74,30),(-100,10)).assemble().finalize().extrude(13))