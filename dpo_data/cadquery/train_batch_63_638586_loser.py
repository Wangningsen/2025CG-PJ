import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-57,0))
w1=cq.Workplane('ZX',origin=(0,-21,0))
r=w0.sketch().arc((-12,-4),(-67,-44),(-11,-79)).arc((63,-73),(21,-9)).arc((17,-8),(12,-8)).arc((17,-5),(21,0)).segment((38,0)).segment((38,67)).segment((-12,67)).close().assemble().push([(-34,73)]).circle(27).finalize().extrude(88).union(w1.sketch().push([(23,53.5)]).rect(32,39).push([(11,69)]).circle(2,mode='s').finalize().extrude(78))