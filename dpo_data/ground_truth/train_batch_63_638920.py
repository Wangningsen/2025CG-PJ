import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-12))
r=w0.sketch().segment((-58,-30),(-56,-36)).arc((-53,-63),(-38,-86)).segment((-35,-93)).segment((-32,-91)).arc((-22,-97),(-12,-100)).segment((-12,-34)).segment((57,-34)).arc((51,-16),(40,-2)).segment((37,4)).segment((34,3)).arc((-18,10),(-54,-29)).close().assemble().push([(37,79)]).circle(21).finalize().extrude(24)