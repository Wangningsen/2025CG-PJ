import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-18))
r=w0.sketch().push([(-36,58.5)]).rect(56,65).push([(78,-33)]).circle(19).circle(9,mode='s').finalize().extrude(-32).union(w0.sketch().push([(-52,55)]).circle(45).push([(-46,-78)]).circle(22).finalize().extrude(68))