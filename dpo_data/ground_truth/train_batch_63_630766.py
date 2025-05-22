import cadquery as cq
w0=cq.Workplane('YZ',origin=(24,0,0))
w1=cq.Workplane('XY',origin=(0,0,-12))
r=w0.sketch().arc((-11,-15),(-31,-60),(-2,-20)).arc((-12,-27),(-11,-15)).assemble().push([(-18.5,-38)]).rect(29,10,mode='s').finalize().extrude(76).union(w1.sketch().push([(-58,4)]).rect(84,78).circle(10,mode='s').finalize().extrude(75))