import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,19))
r=w0.sketch().push([(15,-12)]).circle(24).push([(-3,-5)]).rect(2,2,mode='s').finalize().extrude(-39).union(w0.sketch().arc((-45,46),(-89,-28),(-3,-18)).arc((21,-17),(35,0)).segment((35,25)).segment((46,25)).arc((47,59),(27,86)).arc((16,98),(-1,97)).arc((-35,83),(-45,46)).assemble().push([(85.5,-62)]).rect(21,76).finalize().extrude(-4))