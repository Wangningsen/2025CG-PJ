import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-37,0))
r=w0.workplane(offset=61/2).moveTo(-79,12).cylinder(61,19).union(w0.sketch().segment((-100,-62),(-58,-62)).segment((-58,-38)).segment((-41,-87)).segment((100,-38)).segment((69,53)).segment((-58,9)).segment((-58,87)).segment((-100,87)).close().assemble().finalize().extrude(75))