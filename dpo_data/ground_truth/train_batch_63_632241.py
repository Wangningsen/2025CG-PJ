import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-32))
w1=cq.Workplane('XY',origin=(0,0,-3))
r=w0.sketch().segment((-40,-89),(45,-89)).arc((89,-82),(54,-55)).segment((54,29)).segment((-40,29)).close().assemble().finalize().extrude(51).union(w0.workplane(offset=52/2).moveTo(36,46).cylinder(52,54)).union(w1.sketch().arc((-90,-19),(-29,-26),(-58,29)).arc((-67,0),(-90,-19)).assemble().finalize().extrude(36))