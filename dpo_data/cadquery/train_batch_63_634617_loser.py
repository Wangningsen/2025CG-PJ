import cadquery as cq
w0=cq.Workplane('YZ',origin=(-13,0,0))
w1=cq.Workplane('XY',origin=(0,0,-70))
r=w0.sketch().push([(-20,-34)]).circle(64).push([(8.5,87.5)]).rect(151,19).push([(8.5,88)]).rect(1,16,mode='s').finalize().extrude(113).union(w1.sketch().segment((-81,-39),(10,-39)).segment((10,29)).segment((-7,29)).arc((-77,62),(-81,-19)).close().assemble().finalize().extrude(92))