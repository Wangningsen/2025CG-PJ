import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-5))
w1=cq.Workplane('YZ',origin=(-7,0,0))
r=w0.sketch().segment((-76,-30),(-56,-49)).segment((-38,-30)).close().assemble().reset().face(w0.sketch().segment((29,-65),(51,-65)).segment((51,-69)).segment((60,-69)).segment((60,-65)).segment((100,-65)).segment((100,-3)).segment((29,-3)).close().assemble()).finalize().extrude(3).union(w0.workplane(offset=74/2).moveTo(-82,-9).cylinder(74,18)).union(w1.workplane(offset=54/2).moveTo(26,-26).cylinder(54,43))