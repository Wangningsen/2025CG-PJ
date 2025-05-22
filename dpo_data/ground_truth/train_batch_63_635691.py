import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-39))
w1=cq.Workplane('YZ',origin=(-15,0,0))
r=w0.sketch().segment((-31,-93),(-4,-93)).segment((-4,-86)).arc((24,-48),(-4,-10)).segment((-4,-3)).segment((-31,-3)).segment((-31,-10)).arc((-58,-48),(-31,-86)).close().assemble().finalize().extrude(57).union(w0.sketch().push([(-85,-40)]).circle(15).reset().face(w0.sketch().segment((-6,64),(37,-27)).segment((98,1)).segment((56,93)).close().assemble()).finalize().extrude(95)).union(w1.workplane(offset=115/2).moveTo(-48,-27).cylinder(115,29))