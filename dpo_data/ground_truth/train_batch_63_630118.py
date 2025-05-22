import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,0))
w1=cq.Workplane('XY',origin=(0,0,32))
r=w0.sketch().segment((-51,33),(8,33)).segment((8,8)).segment((25,8)).segment((25,9)).arc((41,16),(34,33)).segment((83,33)).segment((83,62)).segment((25,62)).segment((25,87)).segment((8,87)).segment((8,62)).segment((-51,62)).close().assemble().finalize().extrude(-14).union(w0.workplane(offset=100/2).moveTo(63,95).cylinder(100,5)).union(w1.sketch().push([(-15.5,-36)]).rect(135,128).push([(16,23)]).circle(3,mode='s').finalize().extrude(-132))