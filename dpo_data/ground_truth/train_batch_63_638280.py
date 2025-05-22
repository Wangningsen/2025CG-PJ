import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,5,0))
w1=cq.Workplane('XY',origin=(0,0,-71))
r=w0.sketch().segment((-83,-3),(-57,-100)).segment((5,-83)).segment((-11,-25)).segment((-11,-7)).segment((-3,13)).arc((5,9),(14,8)).arc((80,7),(36,55)).arc((14,66),(-7,57)).segment((-11,58)).segment((-11,76)).segment((-23,76)).segment((-23,46)).segment((-38,9)).close().assemble().push([(-39,-43.5)]).rect(18,41,mode='s').finalize().extrude(-69).union(w1.sketch().push([(55.5,20)]).rect(89,88).push([(56,20)]).circle(43,mode='s').finalize().extrude(3))