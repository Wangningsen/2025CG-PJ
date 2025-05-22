import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-59))
w1=cq.Workplane('ZX',origin=(0,33,0))
r=w0.sketch().arc((-36,74),(-100,-1),(-33,-74)).segment((-33,-71)).arc((-21,-72),(-9,-71)).segment((-9,-74)).arc((52,1),(-13,74)).segment((-13,71)).arc((-26,72),(-36,71)).close().assemble().finalize().extrude(118).union(w1.sketch().push([(-29,84)]).circle(16).push([(-36,80)]).circle(3,mode='s').finalize().extrude(-92))