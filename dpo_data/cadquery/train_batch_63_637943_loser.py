import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,60))
r=w0.workplane(offset=-160/2).moveTo(28,-27).cylinder(160,54).union(w0.sketch().arc((-73,51),(-82,24),(-72,-3)).close().assemble().reset().face(w0.sketch().arc((-65,-12),(-24,-22),(12,-3)).close().assemble()).reset().face(w0.sketch().segment((-11,63),(18,43)).arc((9,65),(-11,81)).close().assemble()).finalize().extrude(40))