import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-5))
w1=cq.Workplane('YZ',origin=(-7,0,0))
r=w0.sketch().segment((29,-65),(49,-65)).arc((65,-69),(80,-65)).segment((100,-65)).segment((100,-6)).segment((80,-6)).arc((65,-2),(49,-6)).segment((29,-6)).close().assemble().finalize().extrude(3).union(w0.sketch().segment((-85,-21),(-56,-49)).segment((-39,-32)).segment((-68,-4)).close().assemble().finalize().extrude(3)).union(w0.workplane(offset=74/2).moveTo(-82,-9).cylinder(74,18)).union(w1.workplane(offset=54/2).moveTo(26,-26).cylinder(54,43))