import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-33))
w1=cq.Workplane('XY',origin=(0,0,-12))
r=w0.sketch().push([(60,36)]).circle(22).reset().face(w0.sketch().segment((49,21),(71,21)).segment((71,23)).segment((62,23)).arc((68,31),(62,40)).segment((71,40)).segment((71,51)).segment((49,51)).segment((49,40)).segment((58,40)).arc((51,31),(58,23)).segment((49,23)).close().assemble(),mode='s').finalize().extrude(133).union(w1.sketch().push([(-57,-33)]).circle(25).push([(-57,-33)]).rect(40,20,mode='s').finalize().extrude(-88))