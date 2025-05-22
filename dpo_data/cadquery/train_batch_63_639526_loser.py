import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().push([(3,-14.5)]).rect(170,147).push([(41,-2)]).circle(47,mode='s').finalize().extrude(-200).union(w0.sketch().push([(-38,36)]).circle(50).reset().face(w0.sketch().segment((-73,18),(-44,-11)).segment((3,33)).segment((-26,62)).close().assemble(),mode='s').finalize().extrude(-164))