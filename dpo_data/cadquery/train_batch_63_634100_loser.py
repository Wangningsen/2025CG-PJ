import cadquery as cq
w0=cq.Workplane('YZ',origin=(1,0,0))
w1=cq.Workplane('XY',origin=(0,0,-43))
r=w0.sketch().arc((22,-10),(24,-12),(25,-15)).segment((100,-15)).segment((100,84)).segment((22,84)).segment((22,69)).arc((66,45),(22,22)).segment((22,17)).arc((-61,18),(22,15)).close().assemble().push([(-29,-58)]).circle(26).finalize().extrude(77).union(w1.sketch().push([(-75.5,-65)]).rect(5,70).push([(-75,-91)]).circle(1,mode='s').finalize().extrude(41))