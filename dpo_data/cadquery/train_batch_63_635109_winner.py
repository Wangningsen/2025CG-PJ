import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-26))
r=w0.sketch().segment((-71,-98),(-68,-100)).segment((-44,-70)).segment((-47,-69)).close().assemble().push([(-45,47.5)]).rect(4,105).push([(18,7)]).circle(53).finalize().extrude(52)