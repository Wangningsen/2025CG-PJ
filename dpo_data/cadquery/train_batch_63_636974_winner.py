import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-53))
r=w0.sketch().arc((15,-36),(72,-36),(35,10)).arc((-16,6),(15,-36)).assemble().finalize().extrude(-45).union(w0.sketch().push([(-23.5,17.5)]).rect(153,31).push([(-24,18)]).circle(7,mode='s').push([(82,36)]).circle(18).finalize().extrude(152))