import cadquery as cq
w0=cq.Workplane('YZ',origin=(14,0,0))
w1=cq.Workplane('XY',origin=(0,0,-21))
r=w0.sketch().segment((-100,27),(-86,13)).segment((-86,-53)).segment((-27,-53)).segment((-24,-56)).segment((-22,-53)).segment((25,-53)).segment((25,-39)).segment((100,-39)).segment((100,56)).segment((25,56)).segment((25,83)).segment((-24,83)).segment((-27,86)).segment((-29,83)).segment((-86,83)).segment((-86,41)).close().assemble().finalize().extrude(-28).union(w1.workplane(offset=-64/2).moveTo(1,46).cylinder(64,7))