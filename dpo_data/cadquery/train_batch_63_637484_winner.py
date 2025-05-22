import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-36))
r=w0.sketch().segment((19,-52),(38,-52)).arc((59,-69),(81,-52)).segment((100,-52)).segment((100,-41)).segment((81,-41)).arc((59,-24),(38,-41)).segment((19,-41)).close().assemble().finalize().extrude(37).union(w0.sketch().arc((-21,19),(-89,-61),(6,-14)).segment((6,82)).segment((-21,82)).close().assemble().finalize().extrude(72))