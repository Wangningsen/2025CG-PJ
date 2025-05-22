import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-4))
r=w0.sketch().segment((-54,-6),(100,-6)).segment((100,35)).segment((-38,53)).segment((-34,88)).segment((-54,88)).close().assemble().finalize().extrude(-87).union(w0.workplane(offset=95/2).moveTo(-69,-57).cylinder(95,31))