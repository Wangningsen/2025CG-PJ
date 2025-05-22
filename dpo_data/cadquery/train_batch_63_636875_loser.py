import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-26,0))
w1=cq.Workplane('ZX',origin=(0,-91,0))
r=w0.sketch().push([(-41,3)]).rect(118,16).push([(36,80)]).rect(128,26).push([(36,80.5)]).rect(68,13,mode='s').finalize().extrude(-29).union(w0.sketch().segment((-10,-93),(22,-93)).arc((13,-77),(22,-60)).segment((-10,-60)).close().assemble().finalize().extrude(118)).union(w1.sketch().push([(-41.5,3)]).rect(91,122).push([(-25,14)]).circle(38,mode='s').finalize().extrude(111))