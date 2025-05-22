import cadquery as cq
w0=cq.Workplane('YZ',origin=(-36,0,0))
r=w0.workplane(offset=-38/2).moveTo(51,-24).box(98,78,38).union(w0.sketch().push([(-63,26)]).circle(37).reset().face(w0.sketch().segment((-70,0),(-62,-6)).segment((-59,-1)).segment((-66,4)).close().assemble(),mode='s').finalize().extrude(110))