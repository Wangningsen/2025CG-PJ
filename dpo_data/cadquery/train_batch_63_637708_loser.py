import cadquery as cq
w0=cq.Workplane('YZ',origin=(-57,0,0))
r=w0.sketch().push([(0,90.5)]).rect(106,19).push([(-24,91)]).circle(6,mode='s').finalize().extrude(-28).union(w0.sketch().push([(-21,-1)]).circle(25).push([(9.5,-52)]).rect(17,96).finalize().extrude(142))