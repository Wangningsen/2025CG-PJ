import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-7))
r=w0.sketch().push([(79,62)]).circle(21).push([(83,73)]).circle(3,mode='s').finalize().extrude(-73).union(w0.sketch().push([(72,-62)]).rect(8,42).push([(71.5,-73)]).rect(3,4,mode='s').finalize().extrude(-57)).union(w0.workplane(offset=88/2).moveTo(-56,-15).box(88,8,88))