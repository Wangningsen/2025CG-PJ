import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-80))
r=w0.sketch().segment((-56,-74),(82,-74)).segment((82,100)).segment((-56,100)).segment((-56,23)).arc((-57,13),(-56,3)).close().assemble().finalize().extrude(123).union(w0.workplane(offset=160/2).moveTo(0,-12).cylinder(160,88))