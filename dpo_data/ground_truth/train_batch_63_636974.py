import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-52))
r=w0.sketch().arc((15,-38),(73,-33),(34,9)).arc((-18,2),(15,-38)).assemble().push([(5.5,-33.5)]).rect(5,5,mode='s').finalize().extrude(-46).union(w0.sketch().push([(-23.5,17.5)]).rect(153,31).push([(-24,18)]).circle(7,mode='s').push([(82,36)]).circle(18).finalize().extrude(151))