import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-13))
w1=cq.Workplane('YZ',origin=(20,0,0))
r=w0.sketch().push([(-69,44)]).circle(31).circle(19,mode='s').push([(9.5,23)]).rect(31,8).finalize().extrude(64).union(w1.sketch().arc((-64,24),(-17,-50),(-14,37)).arc((-45,50),(-64,24)).assemble().finalize().extrude(80))