import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,22))
w1=cq.Workplane('XY',origin=(0,0,0))
r=w0.sketch().segment((-31,15),(-5,15)).segment((-5,3)).segment((27,3)).segment((27,15)).segment((52,15)).segment((52,88)).segment((27,88)).segment((27,100)).segment((-5,100)).segment((-5,88)).segment((-31,88)).close().assemble().push([(11,52)]).circle(32,mode='s').finalize().extrude(-119).union(w0.workplane(offset=49/2).moveTo(11,52).cylinder(49,5)).union(w1.workplane(offset=97/2).moveTo(-26,-74).cylinder(97,26))