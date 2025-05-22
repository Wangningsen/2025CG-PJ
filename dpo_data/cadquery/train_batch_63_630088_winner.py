import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-38))
w1=cq.Workplane('XY',origin=(0,0,-48))
r=w0.sketch().segment((-100,-73),(-95,-76)).segment((-92,-69)).segment((-97,-67)).close().assemble().finalize().extrude(86).union(w1.sketch().segment((-2,-36),(38,-36)).segment((38,-50)).arc((100,15),(44,76)).segment((44,75)).segment((42,75)).segment((42,76)).arc((-21,36),(-2,-36)).assemble().push([(70.5,56.5)]).rect(13,5,mode='s').finalize().extrude(60))