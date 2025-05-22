import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-12))
r=w0.sketch().segment((-50,-41),(14,-100)).segment((54,-56)).segment((-11,4)).close().assemble().push([(0,60)]).circle(19).finalize().extrude(-58).union(w0.sketch().push([(0,60)]).rect(108,80).rect(82,62,mode='s').finalize().extrude(82))