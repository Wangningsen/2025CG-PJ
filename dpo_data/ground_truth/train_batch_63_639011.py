import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-12))
r=w0.sketch().segment((-51,-41),(14,-100)).segment((54,-56)).segment((-11,4)).close().assemble().push([(0,60)]).circle(19).finalize().extrude(-58).union(w0.sketch().push([(0,60)]).rect(108,80).push([(-0.5,60)]).rect(83,62,mode='s').finalize().extrude(82))