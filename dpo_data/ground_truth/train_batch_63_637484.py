import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-36))
r=w0.sketch().segment((20,-52),(38,-52)).arc((60,-69),(82,-52)).segment((100,-52)).segment((100,-41)).segment((82,-41)).arc((60,-24),(38,-41)).segment((20,-41)).close().assemble().finalize().extrude(37).union(w0.sketch().arc((-21,19),(-88,-62),(6,-14)).segment((6,82)).segment((-21,82)).close().assemble().finalize().extrude(72))