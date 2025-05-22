import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-59,0))
w1=cq.Workplane('ZX',origin=(0,-77,0))
r=w0.sketch().segment((-62,-86),(-31,-86)).segment((-31,-19)).arc((0,-28),(31,-19)).segment((31,-95)).segment((53,-95)).segment((53,11)).arc((51,50),(29,75)).segment((29,36)).segment((-52,36)).segment((-52,47)).arc((-56,25),(-52,3)).segment((-62,3)).close().assemble().finalize().extrude(145).union(w1.sketch().push([(0,27)]).rect(200,136).push([(-62,73)]).circle(27,mode='s').finalize().extrude(-13))