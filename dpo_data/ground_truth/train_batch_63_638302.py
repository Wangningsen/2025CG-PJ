import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-51,0))
w1=cq.Workplane('XY',origin=(0,0,9))
r=w0.sketch().segment((-25,0),(-21,0)).arc((-5,-12),(10,0)).segment((29,0)).segment((29,30)).segment((-25,30)).close().assemble().finalize().extrude(-46).union(w1.sketch().arc((-60,69),(-68,37),(-58,5)).segment((-58,-100)).segment((68,-100)).segment((68,5)).segment((46,5)).arc((39,80),(-35,93)).arc((-35,68),(-60,69)).assemble().push([(-25,-70)]).circle(19,mode='s').finalize().extrude(-38))