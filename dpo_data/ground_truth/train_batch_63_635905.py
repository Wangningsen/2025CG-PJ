import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,43))
r=w0.workplane(offset=-99/2).moveTo(-64,-63).cylinder(99,31).union(w0.sketch().arc((-79,-23),(-39,-60),(15,-48)).segment((100,-48)).segment((100,40)).segment((54,40)).segment((54,94)).segment((-42,94)).segment((-42,52)).arc((-57,44),(-70,32)).arc((-100,9),(-79,-23)).assemble().finalize().extrude(13))