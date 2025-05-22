import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-32))
w1=cq.Workplane('XY',origin=(0,0,-4))
r=w0.sketch().segment((-40,-89),(45,-89)).arc((89,-81),(54,-55)).segment((54,29)).segment((-40,29)).close().assemble().finalize().extrude(51).union(w0.workplane(offset=51/2).moveTo(36,46).cylinder(51,54)).union(w1.sketch().arc((-62,2),(-87,-24),(-52,-34)).arc((-27,-9),(-42,22)).segment((-42,28)).segment((-50,28)).segment((-50,24)).arc((-59,16),(-62,2)).assemble().finalize().extrude(36))