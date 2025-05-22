import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,32,0))
r=w0.workplane(offset=-65/2).moveTo(-62.5,61).box(75,58,65).union(w0.sketch().arc((-18,7),(4,-77),(58,-8)).arc((5,-17),(-1,36)).arc((-13,23),(-18,7)).assemble().reset().face(w0.sketch().arc((13,46),(38,47),(57,33)).segment((100,33)).segment((100,83)).segment((13,83)).close().assemble()).push([(62,-83)]).circle(7).finalize().extrude(-23))