import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-5))
w1=cq.Workplane('YZ',origin=(-7,0,0))
r=w0.sketch().segment((-74,-22),(-56,-48)).segment((-39,-36)).segment((-57,-10)).close().assemble().reset().face(w0.sketch().segment((29,-65),(48,-65)).arc((64,-69),(79,-65)).segment((100,-65)).segment((100,-6)).segment((79,-6)).arc((64,-2),(48,-6)).segment((29,-6)).close().assemble()).finalize().extrude(3).union(w0.workplane(offset=74/2).moveTo(-82,-9).cylinder(74,18)).union(w1.workplane(offset=54/2).moveTo(26,-26).cylinder(54,43))